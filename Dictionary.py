# Collection of key : value pairs
# map key to values
# Phonebook (dictionary) : name (key) -> contact details (value)
# Ordered , Changeable , No duplicates
point = {"x": 1, "y": 2}  # syntax 1
# key -> only immutable ( string , number , tuple) + unique
# immutable : An object whose internal state cannot be changed after creation

point1 = dict(x=1, y=2)  # syntax 2
print(point["x"])
point["x"] = 10
point["z"] = 20
# print(point["a"])         #error as not available
print(point.get("a"))  # returns none
print(point.get("a", 0))  # 0 set as default return if a not found
del point["x"]
print(point)
# loop over dictionary
for key in point:
    print(key, point[key])

for key, value in point.items():  # returns tuples that is unpacked to key and value
    print(key, value)

# DICTIONARY COMPREHENSION

values = []
for x in range(5):
    values.append(x * 2)

values = [x * 2 for x in range(5)]  # same as 28-30
value_set = {x * 2 for x in range(5)}  # set comprehension
value_dictionary = {x: x * 2 for x in range(5)}  # dictionary comprehension
# val_tup = (x*2 for x in range(5))   # we get generator obj
