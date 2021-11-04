import csv
import math

#######################################################################
#######################################################################
######### MAIN DICT SECTION



def open_file():
    dept_vals = []
    with open('Company_DB - Sheet1.csv') as db:
        company_db = list(csv.reader(db))
        dict_keys = company_db[0]
        item_list = []
        final_dict = []

        for row in company_db[1:]:
            # print(row)
            new_dict = {}
            for num in range(len(dict_keys)):
                if dict_keys[num] == 'start date':
                    dict_keys[num] = 'startdate'
                    item_list = []
                    row[num] = row[num].split('/')
                    for item in row[num]:
                        item_list.append(item)
                    row[num] = item_list
                    # print(row[num])

                elif dict_keys[num] == 'gender':
                    row[num] = row[num].lower()
                elif dict_keys[num] == 'department':

                    dept_vals.append(row[num])

                new_dict[dict_keys[num]] = row[num]

            final_dict.append(new_dict)

        return dept_vals, final_dict, dict_keys



dept_vals, final_dict, dict_keys = open_file()

valid_dict = {'department': ['==', '='], 'age' : ['>', '<', '==', '=', '>=', '<='], 'gender' : ['==', '='], 'startdate': ['>', '<', '==', '=', '>=', '<='], 'salary' : ['>', '<', '==', '=', '>=', '<=']}

gender_vals = ['m', 'f']

valid_queries = dict_keys




# print(valid_queries, valid_dict, dept_vals)

#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################


def calculate(month, day, year):

    total_days = year + month + day

    return total_days



def evaluation(main_query, final_dict):
    main_query = main_query.split()

    token1 = main_query[0]
    token2 = main_query[1]
    token3 = main_query[2]




    if token2 == '=':
        token2 = '=='

    if token1.lower() == 'startdate':
        token3 = token3.split('/')
        user_total = calculate(token3[0], token3[1], token3[2])

        for item in final_dict:
            data_date = item[token1]
            # data_date.split('/')
            print(data_date)
            data_total = calculate(data_date[0], data_date[1], data_date[2])
            # print(f'user: {user_total}')
            print(f'comp: {data_total}')
            # if eval(f'"{data_total}" {token2} "{user_total}"'):
            #     print(item)

    else:
        for item in final_dict:
            if eval(f'"{item[token1].lower()}" {token2} "{token3}"'):
                print(item)






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
    while value_c == 0:
        for key, value in valid_dict.items():
            if key == token1.lower():
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
    # print(department_vals)

    if token1.lower() == 'age' or token1.lower() == 'salary':
        if token3.isdigit():
            valid = True
        else:
            valid = False

    elif token1.lower() == 'startdate':
        if len(token3.split('/')) == 3:
            valid = True
        else:
            valid = False




    elif token1.lower() == 'department':
        for value in department_vals:

            if value.lower() == token3.lower():
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
    valid = True
    token1 = 0
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



main_query = main(valid_queries, valid_dict, dept_vals)
# main_query = main_query.split()
print(main_query)

if main_query:
    evaluation(main_query, final_dict)


# for record in dict_list:
    # equation = f'{record[main_query[0]]} {main_query[1]} {main_query[2]}'
    # print(equation)

    # if eval(equation):
    #     print(record)


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
