def magic(a):
        if a[1] in ('+', '-', '*', '/', '**', '%'):
            x = float(a[0])
            y = float(a[2])
            if a[1] == '+':
                ans=(x + y)
            elif a[1] == '-':
                ans=(x - y)
            elif a[1] == '*':
                ans=(x * y)
            elif a[1] == '/':
                if y != 0:
                    ans=(x / y)
                else:
                    ans="Деление на ноль!"
            elif a[1] == '**':
                ans=x**y
            elif a[1] == '%':
                ans=x%y
        else:
            ans="Неверный знак операции!"
        return ans

s=input('Введите что нужно посчитать ').split()

print(s)
print(magic(s))



