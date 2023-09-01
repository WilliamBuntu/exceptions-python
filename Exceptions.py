filename = './test.txt'
filename1 = './test1.txt'

try:
   file = open(filename, 'r')
   content = file.read()
   print(content)

finally:
    file.close()


# try:
with open(filename1, 'r') as file:
        content_1 = file.read()
        print(content_1)

# except FileNotFoundError:
#     print('FileNotFoundError found')
# except ZeroDivisionError:
#     print("ZeroDivisionError")


# except NameError:
#     print("NameError : y must be a number")

# to install a package
# pip install 'packages'
# pip install -U packages
# pip show package
