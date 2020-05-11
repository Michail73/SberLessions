a=list(input('Put digits '))
answer = []

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        answer.append(a[i+1])

print(answer)
