n=int(input('Put length of stairway '))

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, sep='', end='')
    print()
