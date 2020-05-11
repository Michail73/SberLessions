n=int(input('Put length of stairway '))

for i in range(1, n+1):
    print(n * ' ', end='')
    for j in range(1,i+1):
        print(j, sep='', end='')
    print()

d=1
for i in reversed(range(1, n+1)):
    #print(d * ' ', end='')
    for s in range(1, i+1):
        print(s, sep='', end='')
    # for j in reversed(range(1, i + 1)):
    #     print(j, sep='', end='')
    print()
    d += 1