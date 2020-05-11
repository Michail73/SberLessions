n=str(input('Put same string '))

s=n.split(' ')
#print(s[0])

#print(n.capitalize())

if n.istitle():
    print(s[0], s[1])
else:
    print(s[0].capitalize(), s[1].capitalize())


