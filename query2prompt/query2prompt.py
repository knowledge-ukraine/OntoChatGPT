# -*- coding: utf8 -*-

import time
import json
import urllib
from SPARQLWrapper import SPARQLWrapper, JSON


class PromptMaker:
    def __init__(self, queries_file="queries.json", settings_file="settings.json"):
        """
        :param queries_file: path and name of the JSON file where the SPARQL queries are stored
        :param settings_file: path and name of the JSON file where the settings are stored
        """
        self.query_templates = json.loads(open(queries_file, 'r').read())
        self.settings = json.loads(open(settings_file, 'r').read())

    def __execute_query__(self, destination, order, language="ukrainian language"):
        """
        :param destination: string - destination of the SPARQL query - which part of the prompt is to be obtained.
                            Possible options: "instructions", "inputs", "outputs".
        :param order: int or string with meaning of int (1, 2, 3 options are possible). It is responsible for the
                      number of the task of the prompt to be formed
                      1 - define intents
                      2 - find named entities
                      3 - make inference basing on contexts and intents
        :param language: string - name of the language of the input to deal with.
                                  Possible options: "ukrainian language", "english language", "russian language".
                                  Lowercase.
        :return: dict - results of the SPARQL query in a form of python dictionary
        """
        output = dict()
        if destination is not None:
            template = self.query_templates.get(str(destination))
            if template is not None:
                if self.settings.get("ontology name") is not None:
                    query = template.replace("[ontology_name_var]", str(self.settings["ontology name"])).replace(
                                      "[task_order_var]", str(order)).replace("[language_var]", str(language))
                    try:
                        sparql = SPARQLWrapper(self.settings["entry point"])
                        sparql.setReturnFormat(JSON)
                        sparql.setQuery(query)
                        results = sparql.query().convert()
                    except urllib.error.URLError:
                        print("Unable to connect to the ontology entry point: ", self.settings["entry point"])
                        return output
                    for item in results['results']['bindings']:
                        for position in results['head']['vars']:
                            if position != 'task_name':
                                if position in item:
                                    if position not in output:
                                        output[position] = [item[position]['value']]
                                    else:
                                        output[position].append(item[position]['value'])
                                else:
                                    if position not in output:
                                        output[position] = [None]
                                    else:
                                        output[position].append(None)
        return output

    def create_prompt(self, input={}, order=1, language="ukrainian language"):
        """
        :param input: dict - input data for the prompt.
        :param order: int or string with meaning of int (1, 2, 3 options are possible). It is responsible for the
                      number of the task of the prompt to be formed
                      1 - define intents
                      2 - find named entities
                      3 - make inference basing on contexts and intents
        :param language: string - name of the language of the input to deal with.
                                  Possible options: "ukrainian language", "english language", "russian language".
                                  Lowercase.
        :return: dict - a structured prompt with the purpose according to the passed "order" parameter.
                        It could be easily converted to JSON.
        """
        onto_data = dict()

        present_intents = [i.get("intent") for i in input.get("intents", [])]

        for destination in self.query_templates:
            onto_data[destination] = self.__execute_query__(destination=destination, order=order, language=language)
        prompt = dict()
        for key in onto_data:
            if 'field_name' in onto_data[key]:
                if key == "instructions":
                    for i, name in enumerate(onto_data[key]['field_name']):
                        f_type = onto_data[key]['field_type'][i]
                        if f_type == 'text field':
                            if name not in prompt:
                                prompt[name] = onto_data[key]['values'][i]
                            else:
                                prompt[name] += ", " + onto_data[key]['values'][i]
                        if f_type == 'list of texts':
                            if name not in prompt:
                                prompt[name] = [onto_data[key]['values'][i]]
                            elif name in prompt and onto_data[key]['values'][i] not in prompt[name]:
                                prompt[name].append(onto_data[key]['values'][i])
                if key == "inputs":
                    for i, name in enumerate(onto_data[key]['field_name']):
                        f_type = onto_data[key]['field_type'][i]
                        set_value = self.settings.get(name)
                        possible_value = onto_data[key]['values'][i]
                        if f_type == 'boolean':
                            if possible_value is not None and possible_value.lower() == 'true':
                                prompt[name] = True
                            else:
                                prompt[name] = False
                        elif f_type == 'number':
                            if set_value is not None:
                                prompt[name] = set_value
                            else:
                                if name in input:
                                    prompt[name] = input[name]
                                else:
                                    prompt[name] = None
                        else:
                            if possible_value is not None and possible_value == set_value:
                                prompt[name] = set_value
                            if possible_value is None:
                                if name in input:
                                    prompt[name] = input[name]
                                else:
                                    prompt[name] = None
                if key == "outputs":
                    if "output representation template" not in prompt:
                        prompt["output representation template"] = {"result": {}}
                    for i, name in enumerate(onto_data[key]['field_name']):
                        f_type = onto_data[key]['field_type'][i]
                        goal_intent = onto_data[key]['for_intent'][i]
                        if goal_intent is None:
                            if f_type == 'text field':
                                if name not in prompt["output representation template"]["result"]:
                                    prompt["output representation template"]["result"][name] =\
                                        onto_data[key]['values'][i]
                                else:
                                    prompt["output representation template"]["result"][name] +=\
                                        ", " + onto_data[key]['values'][i]
                            if f_type == 'list of texts':
                                if name not in prompt["output representation template"]["result"]:
                                    prompt["output representation template"]["result"][name] =\
                                        [onto_data[key]['values'][i]]
                                elif name in prompt and onto_data[key]['values'][i] not in prompt[name]:
                                    prompt["output representation template"]["result"][name].append(
                                        onto_data[key]['values'][i])
                        elif goal_intent in present_intents:
                            if goal_intent not in prompt["output representation template"]["result"]:
                                prompt["output representation template"]["result"][goal_intent] = dict()
                            if name not in prompt["output representation template"]["result"][goal_intent]:
                                prompt["output representation template"]["result"][goal_intent][name] = \
                                    onto_data[key]['values'][i]
                            else:
                                prompt["output representation template"]["result"][goal_intent][name] +=\
                                    ", " + onto_data[key]['values'][i]

        if "output representation template" in prompt and len(present_intents) == 0:
            prompt["output representation template"]["result"] = [prompt["output representation template"]["result"]]

        return prompt

    def name_input_fields(self, order=1, language="ukrainian language"):
        """
        :param order: int or string with meaning of int (1, 2, 3 options are possible). It is responsible for the
                      number of the task of the prompt to be formed
                      1 - define intents
                      2 - find named entities
                      3 - make inference basing on contexts and intents
        :param language: string - name of the language of the input to deal with.
                                  Possible options: "ukrainian language", "english language", "russian language".
                                  Lowercase.
        :return: dict - fields of the prompt to be substituted with input information and their appropriate format
        """
        onto_data = self.__execute_query__(destination="inputs", order=order, language=language)
        output = dict()
        if "field_name" in onto_data:
            for n, field in enumerate(onto_data["field_name"]):
                if field not in self.settings and onto_data["values"][n] is None:
                    if field not in output:
                        output[field] = onto_data["field_type"][n]
                    else:
                        output[field] = [output[field]].append(onto_data["field_type"][n])
        return output


if __name__ == "__main__":
    # Just for the functions test
    start_time = time.time()
    pm = PromptMaker()
    print("Init time: ", time.time() - start_time)
    start_time = time.time()
    print(pm.create_prompt(input={"contexts": ["dfsdf", "sdfsdfs"], "intents": [
            {
                "intent": "subject",
                "type": "narration",
                "probability": 0.6,
                "subject": "основне джерело смертності",
                "object": ""
            },
            {
                "intent": "place",
                "type": "narration",
                "probability": 0.3,
                "subject": "",
                "object": "розвинені країни"
            },
            {
                "intent": "object",
                "type": "interrogation",
                "probability": 0.08,
                "subject": "",
                "object": "смертність"
            },
            {
                "intent": "quantity",
                "type": "imperative",
                "probability": 0.02,
                "subject": "",
                "object": "кількість смертей"
            }
        ]
        }, order=3, language="ukrainian language"))
    print("execution time: ", time.time() - start_time)
    print()
    start_time = time.time()
    print(pm.create_prompt(input={"text": "Сколько хвстов у собаки?"}, order=2, language="ukrainian language"))
    print("execution time: ", time.time() - start_time)
    print()
    start_time = time.time()
    print(pm.create_prompt(input={"input information": "Сколько хвстов у собаки?"},
                           order=1, language="ukrainian language"))
    print("execution time: ", time.time() - start_time)
    print()
    start_time = time.time()
    print(pm.name_input_fields(order=1, language="ukrainian language"))
    print("execution time: ", time.time() - start_time)
    print()
    start_time = time.time()
    print(pm.name_input_fields(order=2, language="ukrainian language"))
    print("execution time: ", time.time() - start_time)
    print()
    start_time = time.time()
    print(pm.name_input_fields(order=3, language="ukrainian language"))
    print("execution time: ", time.time() - start_time)
