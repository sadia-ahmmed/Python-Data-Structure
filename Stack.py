# LIFO -> LAST IN FIRST OUT

browsing_session = []

# append to add at the last
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
print(browsing_session)
last = browsing_session.pop()  # eliminates the last
print(last)
print(browsing_session)
print("redirect ", browsing_session[-1])  # goes to last item
# check if stack is empty or not, if yes then disable
# falsly value -> 0, "" , []
if not browsing_session:
    print("disable")
