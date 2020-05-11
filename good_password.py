s=str(input('Put password '))

l, u, p, d = 0, 0, 0, 0


if (len(s) >= 12):
    for i in s:

        # counting lowercase alphabets
        if (i.islower()):
            l += 1

            # counting uppercase alphabets
        if (i.isupper()):
            u += 1

            # counting digits
        if (i.isdigit()):
            d += 1

            # counting the mentioned special characters
        if (i == '@' or i == '$' or i == '_'):
            p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 ):
    print('Красавчик')
else:
    print('пошел ты нахуй')


