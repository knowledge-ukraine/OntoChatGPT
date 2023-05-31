# Data for "OntoChatGPT Information System: Ontology-Driven Structured Prompts For ChatGPT Meta-Learning" paper

| **meta_ontology.owl**                  | OWL ontology which contains patterns of the structured JSON prompts for the chat GPT content and formation. |
| -------------------------------------- | ------------------------------------------------------------ |
| **terms.json and semantic_graph.json** | Examples of the terms/contexts ontology description organization approaches in the JSON format. |
| **SPARQL-queries-to-meta-ontology.md** | SPARQL queries to obtain from the meta-ontology information about structured JSON prompts for the ChatGPT formation. There are three queries: to get the instructions fiends, to get the information about the input fiends, and to get the response results structure. The input variable of the queries is value of the *task_order* and *language*, which determine the prompt structure (presence of the certain fields and their values). |
| **prompts-samples.md**                 | Examples of the structured JSON prompts for the ChatGPT for the purposes of intents detection, named entities extraction and obtaining inferences from the given contexts and intents. |
| **test-results.md**                    | Table with test questions (in Ukrainian), responses of the ChatGPT to each of the three prompts including the final response, and evaluations of the obtained answers. |
| **figure1.drawio**                     | Figure 1 source - C4 Context/Container diagram.              |

