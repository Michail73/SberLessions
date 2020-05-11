n=int(input('Put length of pyramid '))

print((n-2)*' ', 1)
d=n-2
for i in range(1, n+1):
        print(d * ' ', end='')
        for s in range(1,i+1):
            print(s, sep='', end='')
        for j in reversed(range(1, i+2)):
            print(j, sep='', end='')
        print()
        d -= 1
        if d==-1:
            break
