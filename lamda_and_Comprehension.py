items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
"""""
Basic Method -> making a new list to include the price
price = []
for item in items:
    price.append(item[1])
print(price)
"""
# Map Function
# Map( lambda func, iterable)
prices = list(map(lambda item: item[1], items))
print(prices)

# Filter Function
# find price >=10

filtered= list(filter(lambda item: item[1]>=10, items))
print(filtered)

# List Comprehensions
prices = [item[1] for item in items]    # same as line 15 but easier
filtered = [item for item in items if item[1]>=10]  # same as line 21 but easier

