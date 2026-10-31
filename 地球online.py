import random
events=['上课','逃课','体力耗尽']
for i in range(3):
    event=random.choice(events)
    print(event)
    if event=='体力耗尽':
        break
    else:
        continue

