import csv
import math


def answer_6():
    print('ADIOS!')


########## QUESTION 1 FUNCTION

def answer_1():
    print('PLEASE HAVE END AGE GREATER THAN START')
    age_start = int(input('Input the start age: '))
    age_end = int(input('Input the end age: '))
    print()
    print()

    for key, value in dict_a.items():
        if int(value) >= age_start and int(value) <= age_end:
            print(f'{key}: {value}')
            print()


############ QUESTION 2 FUNCTION

def answer_2():
    print('PLEASE ENTER \'M\' OR \'F\' FOR EMPLOYEE GENDERS')
    get_gender = input('SUBMIT: ')
    get_gender = get_gender.upper()
    print()

    for key, value in dict_g.items():
        if value == get_gender:
            print(f'{key}: {value}')


######### QUESTION 3 FUNCTION

def answer_3y():
    counter = 0
    base = 0
    min_base = math.inf
    max_base = 0

    for key, value in dict_s.items():
        value = int(value)
        counter += 1
        base += value

        if value > max_base:
            max_base = value

        if value < min_base:
            min_base = value
    average_salary = base / counter

    print(f'Average salary: {average_salary}\nMaximum salary: {max_base}\nMinimum salary: {min_base}')


def answer_3n():
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

def answer_3():


    q3 = input('Do you want to see the company salary statistics:(Y) or a specific range of salaries:(N)?\n Submit: ')
    q3 = q3.lower()



    if q3 == 'y':
        answer_3y()

    else:
        answer_3n()



########## QUESTION 4 FUNCTION


def months(x):
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        days = 31
    elif x == 4 or x == 6 or x == 9 or x == 11:
        days = 30
    else:
        days = 28
    return days

def calculate(month, day, year):

    total_days = months(month) + day + (year*365)

    return total_days




def database_calculate(total_days, time):
    counter = 0
    months = 0
    days = 0
    years = 0
    for key, value in dict_start.items():

        for num in value.split('/'):
            counter += 1
            if counter == 1:
                months = int(num)
            elif counter == 2:
                days = int(num)
            else:
                years = int(num)
        database_val = calculate(months, days, years)

        if time == 'b':
            if database_val <= total_days:
                print(f'{key}: {value}')
        else:
            if database_val >= total_days:
                print(f'{key}: {value}')



def answer_4():
    counter = 0
    months = 0
    days = 0
    years = 0

    q4a = input('Input a start date in the format MM/DD/YYYY: ')
    q4a = q4a.split('/')

    q4b = input('Do you want all dates PRIOR: \'B\' or AFTER: \'A\'    : ')
    q4b = q4b.lower()

    for num in q4a:
        counter += 1
        if counter == 1:
            months = int(num)
        elif counter == 2:
            days = int(num)
        else:
            years = int(num)

    total_days = calculate(months, days, years)

    database_calculate(total_days, q4b)



########### ANSWER 5 FUNCTION

def answer_sales(q5):
    for key, value in dict_d.items():
        if value.lower() == q5:
            print(f'{key}: {value}')

def answer_software(q5):
    for key, value in dict_d.items():
        if value.lower() == q5:
            print(f'{key}: {value}')

def answer_management(q5):
    for key, value in dict_d.items():
        if value.lower() == q5:
            print(f'{key}: {value}')


def answer_5():
    q5 = input('Enter the department you want to search for: Sales, Software, or Management: ')
    q5 = q5.lower()

    if q5 == 'sales':
        answer_sales(q5)

    if q5 == 'software':
        answer_software(q5)

    if q5 == 'management':
        answer_management(q5)


######### MAIN DICT SECTION

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

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################

valid = True

valid_queries = ['department', 'age', 'gender', 'startdate', 'salary']

valid_dict = {'department': ['==', '='], 'age' : ['>', '<', '==', '='] , 'gender' : ['==', '='], 'startdate': ['>', '<', '==', '='] , 'salary' : ['>', '<', '==', '=']}


department_vals = ['sales', 'software', 'management']

gender_vals = ['m', 'f']



#### METHODS

def finish(valid, user_query = []):

    if valid:
        new_userquery = user_query[0] + ' ' + user_query[1] + ' ' + user_query[2]
        print(valid, new_userquery)
        return new_userquery
    else:
        print(valid, user_query)



def test1(token1,valid_queries):
    global valid
    for value in valid_queries:
        if token1.lower() == value:
            valid = True
            break
        else:
            valid = False


    return valid



def test2(token1, token2, valid_dict):
    global valid
    value_c = 0

    for key, value in valid_dict.items():
        if key == token1.lower() and value_c == 0:
            for val in value:
                if val == token2:
                    valid = True
                    value_c = 1
                    break

                else:
                    valid = False

    return valid



def test3(token1, token3, department_vals, gender_vals):
    global valid

    if token1.lower() == 'age' or token1.lower() == 'salary' or token1.lower() == 'startdate':
        if token3.isdigit():
            valid = True
        else:
            valid = False

    elif token1.lower() == 'department':
        for value in department_vals:
            if value == token3.lower():
                valid = True
                break
            else:
                valid = False

    else:
        for value in gender_vals:
            if value == token3.lower():
                valid = True
                break
            else:
                valid = False

    return valid

def transition(token4):
    global valid

    if token4.lower() == 'and':
        pass

    elif token4.lower() == 'or':
        pass

    else:
        valid = False

    return token4.lower()



def main(valid_queries, valid_dict, department_vals):
    global valid
    global user_string_query
    counter_or = 0
    counter_and = 0

    query = input('Find all records with: ')


    user_query = query.split()
    size = len(user_query)


    if size == 7:

        token1 = user_query[0]
        token2 = user_query[1]
        token3 = user_query[2]

        token4 = user_query[3]

        token5 = user_query[4]
        token6 = user_query[5]
        token7 = user_query[6]

        if valid and transition(token4) == 'or':
            if test1(token1, valid_queries) or test1(token5, valid_queries):
                counter_or = 1
                if test2(token1, token2, valid_dict) or test2(token5, token6, valid_dict):
                    counter_or = 2
                    if test3(token1, token3, department_vals, gender_vals) or test3(token5, token7, department_vals,gender_vals):
                        counter_or = 3
                        user_string_query = finish(valid, user_query)

            if counter_or != 3:
                finish(valid)



        elif valid and transition(token4) == 'and':
            if test1(token1, valid_queries) and test1(token5, valid_queries):
                counter_and = 1
                if test2(token1, token2, valid_dict) and test2(token5, token6, valid_dict):
                    counter_and = 2
                    if test3(token1, token3, department_vals, gender_vals) and test3(token5, token7,department_vals,gender_vals):
                        counter_and = 3
                        user_string_query = finish(valid, user_query)

            if counter_and != 3:
                finish(valid)


    elif size == 3:
        size3_counter = 0
        token1 = user_query[0]
        token2 = user_query[1]
        token3 = user_query[2]

        if valid and test1(token1, valid_queries):
            size3_counter = 1
            pass
        if valid and test2(token1, token2, valid_dict):
            size3_counter = 2
            pass
        if valid and test3(token1, token3, department_vals, gender_vals):
            size3_counter = 3
            user_string_query = finish(valid, user_query)

        if size3_counter != 3:
            finish(valid)
    else:
        print('ERROR WITH THE LENGTH OF QUERY')
        valid = False
        finish(valid)

    if valid:

        return user_string_query



if main(valid_queries, valid_dict, department_vals):

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################










##### PROJECT DATABASE!!!

######## QUESTION 6 FUNCTION





# question = int(input('		To get information about employee age type:  1\n		To get information about employee gender type:  2\n		To get information about employee salary type: 3\n		To get information about employee start date type: 4\n		To get information about employee department type: 5\n		To exit the database query type: 6\nWhat kind of information do you wish to extract : '))

#### EXIT

# if question == 6:
#     answer_6()
#
#
# ####### AGE
#
#
# elif question == 1:
#     answer_1()
#
#
# ####### GENDER
#
# elif question == 2:
#     answer_2()
#
#
# ###### SALARY
#
# elif question == 3:
#     answer_3()
#
#
# ######## EMPLOYEE START DATE
#
# elif question == 4:
#     answer_4()
#
#
#
#
# # DEPARTMENT
#
# elif question == 5:
#     answer_5()







# record = {}
# record['age'] = 55
# token = ['age', '>', '45']
# # query_str = "record["+"'" + token[0] + "'" + "]" + " " + token[1] + ' ' + token[2]
# query_str = f'record[\'{token[0]}\'] {token[1]} {token[2]}'
# print(query_str)
#
# if eval(query_str):
#     print(record)


