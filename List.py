# define list by [ ]

letters = ["a", "b", "c", "d"]
print(letters[0])  # print specific  items of the list
print(letters[-1])  # -1 indicates the end item of the list
print(letters[0:3])  # accessing custom sequence of list
print(letters[::2])  # returns every second element

# 2D list or Matrix

matrix = [[0, 1], [2, 3]]  # each item is a list

# List of multiple zeros

zeroList = [0] * 5
print(zeroList)

# combine list of different data types

combined = zeroList + letters
print(combined)

# list from 0 till 20
num = list(range(20))
print(num)
print(num[::2])  # returns even numbers
print(num[::-1])  # reverses the list

# make a list from string

chars = list("Hello World")  # imputs the string to a list of chars
print(chars)

# find len of list
print(len(chars))

# LIST UNPACKING: unpacking list to different variables

numbers = [1, 2, 3]
# first , second = numbers          #shows ValueError: too many values to unpack
first, second, third = numbers  # unpacks every time , will show error if no. of variables are less than the length of list
one, two, *others = num  # unpacks the first two digits and repacks the rest of items in the *others* list
print(one, others)
begin, *middle, end = num  # unpacks first and last numbers and packs the whole list in *other* list

# LOOP OVER LIST

# using for loop
for letter in letters:
    print(letter)

# get index and value
for letter in enumerate(letters):
    print(letter)  # returns tuple [ index, value]

# unpacking tuples
for index, letter in enumerate(letters):
    print(index, letter)

# ADDING AND REMOVING ITEMS

# add
letters.append("e")  # adds at end of the list
letters.insert(0, "-")  # adds at a specific index
print(letters)

# remove
letters.pop()        # removes at end of the list
print(letters)
letters.pop(0)       # removes at a specific index
print(letters)
letters.remove("b")  # if index in unknown, deletes the first of given value
print(letters)
del letters[0:2]     #can delete range of items unlike pop method
print(letters)
letters.clear()      #deletes all items in the list
print(letters)

letters = ["a", "b", "c"]
# find index
print(letters.index("c"))
#find a value is not present in the list it would show error. So we need to check it first
if "d" in letters:
    print(letters.index("d"))       # gives no error because of the checking

#find number of value present
print(letters.count("a"))

#Sorting in ascending order
numberlist = [3,51,2,8,6]
numberlist.sort()
print(numberlist)

#Sorting in descending order

numbers.sort(reverse=True)
print(numberlist)