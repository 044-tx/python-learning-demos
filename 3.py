import random
cards=['A','B','C','D','E','F','G','H']
card=random.choice(cards)
with open('result.txt','w',encoding='utf-8') as f:
 f.write(card)