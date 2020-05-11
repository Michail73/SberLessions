length=int(input('Put length of array '))

i=0
a=0
b=0
while i<length:
    digit=int(input())
    i+=1
    a=digit+a
    if digit == 0:
        b += 1

print('Sum of inputed digits: ', a)
print('Amount of input digits, that equals zero: ', b)