from sys import getsizeof

values = (x * 2 for x in range(1000))
print("gen size: ", getsizeof(values))
valuelist = [x * 2 for x in range(1000)]
print("list size: ", getsizeof(valuelist))
"""
print(values)
for x in values:
    print(x)
"""

# type gen doesnot have any length because we only get it after iteration

# should not store in memory if not necessary
# Generator Object (iterable) -> each iteration they generate new value
