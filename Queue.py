# FIFO -> first in, first out
# list to implement queue
# module is a bucket with full of codes

from collections import deque

queue = deque([])  # deque has important function
# add item
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# pop queue
queue.popleft()
print(queue)

# check for empty queue
if not queue:
    print("empty queue")
