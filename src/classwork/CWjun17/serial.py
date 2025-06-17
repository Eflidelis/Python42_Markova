# сериализация и десериализация данных
# виды
# бинарная - данные собир в некую последоват структуру, состоящую из чисто байтовой последовательности
# (самая защищенная)
#текстовая сериализация (JSON, XML - от него произошли все языки разметки)

import json

{
  "key" : "value",
  "string" : 15,

  "key_1" : "string",
  "key_2" : 10,
  "key_3" : 3.14,
  "key_4" : True,
  "key_5" : {
      "key_obj_1" : 1,
      "key_obj_2" : 2,
      "key_obj_3" : 3

  },
    "key_6" : [
        "value",
        "value_1",
        "value_2"
    ],

    "total" :
        {
            # все формы ключей сюда и вперемешку один в другой можно
        }
}
#
#
#
#
#
file = open("example.json", "r", encoding="utf-8")
json_obj = json.load(file)
print(json_obj)
print(json_obj["key_5"]["key_obj_2"])

file.close()

file = open("example.json", "w", encoding="utf-8")
json.dump(json_obj, file, ensure_ascii=False, indent=4)
JSON = (json.dumps(json_obj, ensure_ascii=False)).replace(" ", "")
print(JSON)
print(type(JSON))

json_object = json.loads(JSON)
print(json_object)
print(type(json_object))

file.close()

#
#
#
##
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



