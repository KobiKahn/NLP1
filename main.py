import csv
import math

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
space = ' '
x = 0
with open('Company_DB - Sheet1.csv') as db:
    company_db = csv.reader(db)

    for row in company_db:
        x += 1
        if x != 1:
            name = (row[0] + ' ' + row[1])
            dict_g[name] = row[2]
            dict_a[name] = row[3]
            dict_start[name] = row[4]
            dict_s[name] = row[5]
            dict_d[name] = row[6]


question = int(input('		To get information about employee age type:  1\n		To get information about employee gender type:  2\n		To get information about employee salary type: 3\n		To get information about employee start date type: 4\n		To get information about employee department type: 5\n		To exit the database query type: 6\nWhat kind of information do you wish to extract : '))
print()
print()
print()

#### EXIT

if question == 6:
    print('Adios!')


####### AGE


elif question == 1:

    print('PLEASE HAVE END GREATER THAN START')
    age_start = int(input('Input the start age: '))
    age_end = int(input('Input the end age: '))
    print()
    print()



    for key, value in dict_a.items():
        if int(value) >= age_start and int(value) <= age_end:
            print(f'{key}: {value}')
            print()


####### GENDER

elif question == 2:
    print('PLEASE ENTER \'M\' OR \'F\' FOR EMPLOYEE GENDERS')
    get_gender = input('SUBMIT: ')
    get_gender = get_gender.upper()
    print()

    for key, value in dict_g.items():
        if value == get_gender:
            print(f'{key}: {value}')


###### SALARY

elif question == 3:
    counter = 0
    base = 0
    average_salary = 0

    min_base = math.inf
    max_base = 0

    q3 = input('Do you want to see the company salary statistics:(Y) or a specific range of salaries:(N)?\n Submit: ')
    q3 = q3.lower()
    for key, value in dict_s.items():
        value = int(value)
        counter += 1
        base += value

        if value > max_base:
            max_base = value

        if value < min_base:
            min_base = value
    average_salary = base / counter


    if q3 == 'y':
        print(f'Average salary: {average_salary}\nMaximum salary: {max_base}\nMinimum salary: {min_base}')

    else:
        lower = input('Enter the lowest salary you want to search: ')
        higher = input('Enter the highest salary you want to search or If you want to search for all salaries higher:(h) or if you want to search for all salaries lower:(l): ')

        lower = int(lower)


        if higher == 'h':
            for key, value in dict_s.items():
                if int(value) >= lower:
                    print(f'{key}: {value}')


        elif higher == 'l':
            for key, value in dict_s.items():
                if int(value) <= lower:
                    print(f'{key}: {value}')

        else:
            higher = int(higher)
            for key, value in dict_s.items():
                if int(value) >= lower and int(value) <= higher:
                    print(f'{key}: {value}')



######## EMPLOYEE START DATE

# elif question == 4:
#     q4a = input('Input a start date in the format MM/DD/YYYY: ')
#     q4a = [q4a]
#
#
#     q4b = input('Do you want all dates PRIOR: B or AFTER: A      : ')
#
#     q4b = q4b.lower()
#
#     if q4b == 'b':
#         for key, value in dict_start.items():
#             for n in value.split():
#                 print(n)


# DEPARTMENT

else:
    q5 = input('Enter the department you want to search for: Sales, Software, or Management: ')
    q5 = q5.lower()

    if q5 == 'sales':
        for key, value in dict_d.items():
            if value.lower() == q5:
                print(f'{key}: {value}')

    if q5 == 'software':
        for key, value in dict_d.items():
            if value.lower() == q5:
                print(f'{key}: {value}')

    if q5 == 'management':
        for key, value in dict_d.items():
            if value.lower() == q5:
                print(f'{key}: {value}')


