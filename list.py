#k=list(input('Put digits '))

k=['90', '45', '3', '43']

i=0

for i in range(0,len(k)):
    if i % 2 == 0:
        print(k[i], sep=' ', end=' ')


