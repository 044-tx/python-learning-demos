import time
import random
live=10
t=1

print('生存还是死亡')
time.sleep(t)
print('这是个值得思考的问题')
time.sleep(t)

choose=input('A.生存\nB.死亡\nC.?')
if choose=='A':
    live+=10
    print('活')
    time.sleep(t)
    print('生存还是死亡')
    choose=input('a.生存\nb.死亡\nc.???')
    if choose=='a':
        live+=10
        print(f'当前生存值：{live}')
    elif choose=='b':
        live-=10
        print('死')
    else:
        print(f'当前生命值：{live}')

elif choose=='B':
    live-=10
    print('死')
else:
    live=random.randint(0,20)
    print(f'当前生命值:{live}')
    time.sleep(t)
    if live>10:
        print('活')
    elif live<=10:
        print('死')
