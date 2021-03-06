m=int(input('Put length of stairway '))

def current_row(n):
    row = []
    for i in range(n):
        if i == 0 or i == n - 1:
            row.append(1)
        else:
            c_row = current_row(n - 1)
            row.append(c_row[i - 1] + c_row[i])
    return row


def triangle(m):
    result = []
    for i in range(m):
        result.append(current_row(i + 1))
    return result

print(triangle(m))