n=int(input('Put length of romb '))

print((n-2)*' ', 1)
d=n-2
for i in range(1, n):
        print(d * ' ', end='')
        for s in range(1,i+1):
            print(s, sep='', end='')
        for j in reversed(range(1, i+2)):
            print(j, sep='', end='')
        print()
        d -= 1
        if d==-1:
            break

d=1
for i in reversed(range(1, n)):
    print(d * ' ', end='')
    for s in range(1, i):
        print(s, sep='', end='')
    for j in reversed(range(1, i + 1)):
        print(j, sep='', end='')
    print()
    d += 1


# print((n-2)*' ', 1)