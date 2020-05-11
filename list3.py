import tests_1 as test


# Функция find_even принимает список list_1
# Необходимо вытащить все элементы списка с четными индексами
# Функция должна возвращать список с этими элементами
# Нулевой элемент считается четным

def find_even(list_1):
    # Вставьте свой код ниже
    even_list=[]
    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
         even_list.append(list_1[i])


    return even_list


if __name__ == '__main__':

    for i in test.cases:
        if find_even(i[1]) == i[2]:
            print("Test #" + str(i[0]) + ': OK!')
        else:
            print("Test #" + str(i[0]) + ': KO!')