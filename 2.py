import random
i=0
j=0
while True:
    i=i+1
    j=random.randint(0,1)
    if j==0:
        print(f'第{i}次查看，提现失败')
    else:
        print(f'第{i}次查看，提现成功')
        break

