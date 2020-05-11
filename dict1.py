from collections import Counter

n=int(input('How much words are you going to input? '))
d=[]

for i in range(n):
    x=input()
    d.append(x)

print(d)

c = Counter(d)

print(c)