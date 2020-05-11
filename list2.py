a=list(input('Put digits '))
answer = []

#for i in range(len(a)-1):
max=max(a)
min=min(a)


print(max)

i=a.index(max)
j=a.index(min)
print(min)

print(i)
print(j)

a.insert(i, min)
a.pop(i+1)
a.insert(j, max)
a.pop(j+1)
print('answer ', a)

