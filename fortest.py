n=int(input('Put length of stairway '))

d=n-1

while d>0:
    p=n-(n-d)
    d-=1
    print(p)


for i in range(1, n+1):
    for s in range(1,i+1):
        print(s, sep='', end='')
    for j in reversed(range(1,i+2)):
        print(j, sep='', end='')
    print()
