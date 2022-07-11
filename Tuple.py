# READ ONLY LIST
# CANNOT MODIFY ANY OBJECT NO ADDITION NO DELETION
# USE TO PREVENT ACCIDENTAL MODIFICATIONS
point1 = ()  # empty tuple
point = (1, 2) + (3, 4)  # concatinating tuple
print(type(point))
print(point)
print(point[0:2])
a, b, c, d = point  # tuple unpacking
if 2 in point:
    print("exists")

# LIST TO TUPLE

point2 = tuple([1, 2])
print(point2)
point3 = tuple("Hello World")
print(point3)
