# best way to work with file

with open('test.txt') as my_file:
    print(my_file.readline())


# in order to read and write to a file we do r+
with open('test.txt', mode='a') as my_file:
    text = my_file.write('hey its me')
    print(text)


# w = write
# r = read
# a = append
# r+ = read and write
# r+ cant create a new file

with open('./app/sad.text', mode='a') as my_file:
    text = my_file.write(':(')
    print(text)

try:
    with open('./app/happy.txt', mode='r') as my_file:
        text = my_file.readline()
        print(text)

except FileNotFoundError as err:
    print(f'file not found: {err}')
    raise err
# error to handle inablity to process d file
except IOError as err:
    print(f"file error: {err}")
    raise err

