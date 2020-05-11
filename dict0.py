x={'Hello' : 'Hi', 'Bye': 'Goodbye', 'List' : 'Array'}

a=(input('Put key '))


print(x.get(a))

def get_key(x, a):
    for k, v in x.items():
        if v == a:
            return k
print(get_key(x,a))

