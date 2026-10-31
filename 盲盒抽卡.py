import random
roles=['a','b','c','d','e','f','g','h']
mine=[]
print(mine)
for i in range(5):
    r=random.choice(roles)
    roles.remove(r)
    mine.append(r)
    print(r)
    print(roles)
    print(mine)

