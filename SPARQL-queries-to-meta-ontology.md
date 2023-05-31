**Instructions**
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX name: <http://www.semanticweb.org/zver/ontologies/2023/4/untitled-ontology-50#>
SELECT ?task_name ?instr_field_name ?field_type_name ?instr_possible_values_name
WHERE {
  ?task name:tasks_order "1". 
  ?current_language rdfs:label "ukrainian language"@en.
  ?task rdfs:label ?task_name. 
  ?task rdf:type name:tasks.  
  ?task name:has_instructios ?instr_field.
  ?instr_field rdfs:comment ?instr_field_name.
  ?instr_field name:has_field_type ?field_type.
  ?field_type rdfs:comment ?field_type_name.
  ?instr_field name:possible_values ?instr_possible_values.
  ?instr_possible_values rdfs:comment ?instr_possible_values_name.
  ?instr_possible_values name:relate_to_task ?task.
  ?instr_possible_values name:relate_to_language ?current_language.
  ?current_language rdf:type name:text_languages.   
}
```
**Inputs**
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX name: <http://www.semanticweb.org/zver/ontologies/2023/4/untitled-ontology-50#>
SELECT ?task_name ?input_field_name ?input_field_type_name ?input_possible_values_names
WHERE {
  ?task name:tasks_order "1".
  ?current_language rdfs:label "ukrainian language"@en.  
  ?task rdf:type name:tasks.
  ?task rdfs:label ?task_name.
  ?current_language rdf:type name:text_languages.
  ?task name:has_input_field ?input_field.
  ?input_field rdfs:comment ?input_field_name.
  ?input_field name:has_field_type ?input_field_type.
  ?input_field_type rdfs:comment ?input_field_type_name.
  OPTIONAL {
  ?input_field name:possible_values ?input_possible_values.
  ?input_possible_values rdfs:comment ?input_possible_values_names.
  }  
}
```
**Outputs**
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX name: <http://www.semanticweb.org/zver/ontologies/2023/4/untitled-ontology-50#>
SELECT DISTINCT ?task_name ?output_field_name ?output_field_type_name ?values ?for_intent
WHERE {
  ?task name:tasks_order "1". 
  ?current_language rdfs:label "ukrainian language"@en.
  ?task rdf:type name:tasks.
  ?current_language rdf:type name:text_languages.
  ?task rdfs:label ?task_name.
  ?task name:has_output ?output_template.
   
  ?output_template name:has_output_field ?output_field.
  ?output_field rdfs:comment ?output_field_name.
  ?output_field name:has_field_type ?output_field_type.
  ?output_field_type rdfs:comment ?output_field_type_name.
  ?output_field name:possible_values ?output_possible_values.
  ?output_possible_values rdfs:comment ?values.
  ?output_possible_values name:relate_to_task ?task.
  ?output_possible_values name:relate_to_language ?current_language.
  ?output_possible_values name:relate_to_output ?output_template.
  OPTIONAL {
    ?output_template name:relate_to_intent ?provided_intent.
    ?provided_intent rdfs:comment ?for_intent.
    ?task name:tasks_order "3".    
  }
}
```
