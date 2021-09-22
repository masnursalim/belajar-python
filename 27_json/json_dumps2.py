import json

# dict
print(json.dumps({"nama": "Nursalim", "umur": 30}))

# list
print(json.dumps(["Toyota", "Honda"]))

# tuple
print(json.dumps(("Apel", "Manggis")))

# string
print(json.dumps("Belajar Python"))

# integer
print(json.dumps(100))

# float
print(json.dumps(11.35))

# boolean True
print(json.dumps(True))

# boolean False
print(json.dumps(False))

# None
print(json.dumps(None))
