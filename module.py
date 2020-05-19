import datetime
import  random
import goodPASS2

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

password=[]

k= random.randrange(12, 30)
#print('k= ', k)

for i in range(k):
    a=random.choice('qweasdzxcrtyfghvbnuiojklm')
    password.append(a)
    password.append(random.choice('QWEASDZXCRTYFGHVBNUIOJKLM'))
    password.append(random.choice('1234567890'))
    password.append(random.choice('!@#$%^&*()-+'))

print(listToString(password))

print(goodPASS2.check(password))