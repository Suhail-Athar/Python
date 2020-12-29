#insert your json string in uglyjason to make it readable.

import json

uglyjson = '{"FirstName":"Suhail","Surname":"Athar","mobile":"9958-154-616"}'

#json.load method converts JSON string to Python Object
parsed = json.loads(uglyjson)

x=json.dumps(parsed, indent=3, sort_keys=True)
print(x)