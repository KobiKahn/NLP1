import csv

def write_file(filename, a_string):
    with open(filename, 'a') as file:
        file.write(a_string)
    return file
# write_file('test1.txt', 'ahfuefihfurwhusfgugf')

def open_file(filename, mode = 'read'):
    with open(filename, 'r') as file:
        if mode == 'readlines':
            text = file.readlines()
        elif mode == 'read':
            text = file.read()
        else:
            text = file.readline()
    return text
# open = open_file('file1.txt')
# print(open)

def print_file(filename):
    file_ = open_file(filename)
    print(file_)

# print_file('file1.txt')

def sumColumn(filename):
    total = 0
    read_int = open_file(filename, 'readlines')
    for int_ in read_int:
        total += int(int_)
    print(total)
# sumColumn('int.txt')

def sum_all(filename):
    total = 0
    int_list = []
    read_int = open_file(filename)
    for num in read_int:
        if num.isdigit():
            total += int(num)
    print(total)

# sum_all('int2.txt')

def read_column(filename, columnNo = 0):
    list_c = []
    columns = open_file(filename, 'readlines')
    for row in columns:
        row = row.split()
        list_c.append(row[columnNo])
    print(list_c)

# read_column('readC.txt')

###FIX THIS ONEEE
word_list = ['better', 'honking']
def countword(filename, words):
    count = 0
    word_list = open_file(filename)
    word_list = word_list.lower().split()

    for word in word_list:
        for letter in word:
            if not letter.isalpha():
                word_list.remove(letter)
    print(word_list)
        # if word == words[0]:
        #     count += 1

    print(count)
# countword('bigwords.txt', word_list)












##### PROJECT DATABASE!!!





dict_g = {}
dict_a = {}
dict_start = {}
dict_s = {}
dict_d = {}

gender_l = []
age_l = []
start_l = []
salary_l = []
dept_l = []

x = 0
with open('Company_DB - Sheet1.csv') as db:
    company_db = csv.reader(db)

    for row in company_db:
        x += 1
        if x != 1:
            dict_g[f'{row[0] , row[1]}'] = row[2]
            dict_a[f'{row[0] , row[1]}'] = row[3]
            dict_start[f'{row[0] , row[1]}'] = row[4]
            dict_s[f'{row[0] , row[1]}'] = row[5]
            dict_d[f'{row[0] ,row[1]}'] = row[6]



# print(dict_g)
# print(dict_a)
# print(dict_start)
# print(dict_s)
# print(dict_d)
question = int(input('		To get information about employee age type:  1\n		To get information about employee gender type:  2\n		To get information about employee salary type: 3\n		To get information about employee start date type: 4\n		To get information about employee department type: 5\n		To exit the database query type: 6\nWhat kind of information do you wish to extract : '))
print()
print()
print()
print()
print()
if question == 6:
    print('Adios!')

elif question == 1:

    print('Please have end age greater than start age')
    age_start = int(input('Input the start age: '))
    age_end = int(input('Input the end age: '))
    print()
    print()



    for key, value in dict_a.items():
        if int(value) >= age_start and int(value) <= age_end:
            print(key, value)

    # print(age_vals)





# print(dict_g)
# print(dict_a)
# print(dict_start)
# print(dict_s)
# print(dict_d)