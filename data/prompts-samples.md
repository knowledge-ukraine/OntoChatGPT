**Define intents**

```json
{
“information to provide”: [“define intents”, “find subjects”, “find objects”],
“text”: “Сколько хвостов у собаки”
“language”: “Russian”,
“input information field”: “text”,
“possible intents”: [“quantity”, “place”, “way of doing”, “object”, “subject”, 					        “action”, “location”, “direction”, “scene of action”, “conditions”, “instrument”, collaborator”, “relation”,
                     “cause”, “sequence”, “origin”],
“several intents”: true,
“intents probability”: true,
“show intent subject”: true,
“max intents number”: 4,
“intents arrange”: “by probability”,
“output format”: “JSON”,
“output representation template”: {
    "result": [
        {
            "intent": "intent name - string",
            “type”: “narration, interrogation or imperative ”,
            "probability": “float value”,
            "subject": " subject of the intent as a name group - string",
            "object": " object of the intent as a name or verb group - string "
        }
    ]
}
}
```

**Response**

```json
{
    "result": [
        {
            "intent": "quantity",
            "type": "interrogation",
            "probability": 0.6,
            "subject": "собака",
            "object": "количество хвостов"
        },
        {
            "intent": "subject",
            "type": "interrogation",
            "probability": 0.3,
            "subject": "собака",
            "object": null
        }
    ]
}
```

------

**Find named entities**

```json
{
	“information to provide”: [“nouns and name groups”, “verbs and verb groups],
	“text”: “Расскажи о молодости Энии”
	“language”: “Russian”,
	“input information field”: “text”,
	“output format”: “JSON”,
	“output representation template”: {
		"result": [
			{
				"words": "lemmatized words for the group",
				“type”: “noun or verb”,
				"main word": “main word of the group, and if it is one word it will	be main”
			}
			]
		}
}
```

**Response**

```json
{
	"result": [
		{
			"words": ["молодость", "Энии"],
			"type": "noun",
			"main word": "молодость"
		},
		{
			"words": ["рассказать"],
			"type": "verb",
			"main word": "рассказать"
		}
	]
}
```

------

**Get information from the contexts**

```json
{
	“information to provide”: [“find relevant information make conclusions for the contexts according to the intents”],
	“language”: “Ukrainian”,
	“input information field”: [“contexts” , “intents”],
	“contexts”: ["Реабілітація Реабілітація, основна стратегія охорони здоровя в системі охорони здоровя З точки зору системи охорони здоровя реабілітація є однією з пяти стратегій охорони здоровя13,14, цілі та показники результативності яких показані в Таблиці II27. З моменту прийняття Декларації в Алма-Аті у 1978, реабілітація вважається основною стратегією охорони здоровя у первинній медичній допомозі, яка спрямована на вирішення основних проблем в сфері здоровя в суспільстві шляхом надання промоційних, превентивних, лікувальних та реабілітаційних послуг28. Виникнення реабілітації, як ключової стратегії охорони здоровя в ХХІ столітті Лікувальні, профілактичні та промоційні стратегії охорони здоровя відповідали за зростання впливу медицини і громадського здоровя протягом більшої частини XIX і XX століть. Але в ближче до кінця минулого століття виникли епідеміологічні проблеми, головним чином через успіхи попередніх десятиліть.",
"Зокрема, населення старіє через поліпшення медичного обслуговування і підвищення виживання при станах, що раніше вважалися смертельними, а хронічні неінфекційні захворювання стали, принаймні, в високорозвинених країнах, основним джерелом смертності28. Як наслідок, в цьому столітті, крім підтримки цілі з профілактики, першочерговою стратегією охорони здоровя стає не стільки лікування, скільки оптимізація функціонування людей, які живуть довше, але мають значно більші обмеження життєдіяльності30,31. Але це природна область реабілітації, метою якої є оптимізація внутрішнього потенціалу здоровя і підсилення сприятливості середовища, з тим щоб у взаємодії результатом було більше функціонування та менше обмежень життєдіяльності. Фактично, демографічні та епідеміологічні реалії соціально трансформували реабілітацію в основну стратегію охорони здоровя ХХІ століття32."
],
	"intents": [
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
	],
	“output format”: “JSON”,
	“output keys language”: “Ukrainian”,
	“output representation template”: {
		"intent": “intent name”,
		“results”: “text or an appropriate data structure of None”
	}
}
```
