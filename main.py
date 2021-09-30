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


with open('Company_DB - Sheet1.csv') as db:
    company_db = csv.reader(db)

    for row in company_db:
        print(row)

