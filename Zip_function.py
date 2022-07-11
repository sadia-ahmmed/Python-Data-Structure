list1=[1,2,3]
list2=[10,20,30]

# Combine 2 list into single list of tuples
# USE ZIP FUNCTION -> gives iterable -> turn it to a list
print(list(zip(list1, list2)))

# also takes strings
# will not print the remaining items  if the size of 2 lists are not equal .

print((list(zip("abc", list1, list2))))
