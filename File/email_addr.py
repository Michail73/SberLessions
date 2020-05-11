def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


# Python program to convert a list to string

# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

f = open('task_file.txt', 'r')
FIO=[]
d=open('edit.txt', 'a+')
d.write('EMAIL, NAME, LAST_NAME, TEL, CITY' + '\n')
for line in f:
     #print(line)
     Fileline_list=list(line.split(','))
     FIO.append(list(Fileline_list[1].split() + Fileline_list[2].split()))

     if len(Fileline_list[3])==8 and len(Fileline_list[1])>2 and len(Fileline_list[2])>2:
         Fileline_list.insert(0, listToString(email_gen(FIO)))
         d=open('edit.txt', 'a+')
         d.write(listToString(listToString(Fileline_list)) + '\n')
         d.close()

     FIO=[]
#print(email_gen(FIO))

# print(strings[2])
# print(FIO)

f.close()