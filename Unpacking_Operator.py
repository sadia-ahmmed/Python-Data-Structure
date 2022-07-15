numbers = [1, 2, 3]
print(numbers)
print(*numbers)  # unpacking
values = list(range(5))
# we can unpack any iterables

value = [*range(5), *"Hello"]
# unpacks and inclues inside list
print(value)
# combine list
first = [1, 2]
second = [3, 4]
combine = [*first, *"Hi", *second, *"Bye"]
print(combine)

# Unpack dictionaries

d1 = {"x": 1}
d2 = {"x": 10, "y": 2}
combined_d = {**d1, **d2, "z": 5}
print(combined_d)
