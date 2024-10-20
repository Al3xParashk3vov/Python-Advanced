from collections import deque
queue = deque()
# name .append to end of queue

while True:
    text = input()
    if text == 'Paid':
        while len(queue):
            print(queue.popleft())
    elif text == 'End':
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(text)
