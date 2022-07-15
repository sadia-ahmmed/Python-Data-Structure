# Collection with no duplicates

numbers = [1, 2, 3, 4, 4, 1]
first = set(numbers)
print(first)  # NO DUPLICATES
second = {4, 5}
# second.add(5)
# second.remove(5)
# len(second)
print("Union : ", first | second)  # union of set
print("Intersection : ", first & second)  # intersection of set
print("Difference : ", first - second)  # difference
print(first ^ second)  # either on first or second set but not both
# set not in sequence and does not support indexing
# check for existence in set
