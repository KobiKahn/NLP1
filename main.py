

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
open = open_file('file1.txt')
print(open)