import json
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
print(json.loads(stringOfJsonData))

python_value= {"name":"chris","age":22,"is_married":None,"friends":["john","doe"],"money":34555.78,}
print(json.dumps(python_value))