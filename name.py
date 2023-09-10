import sys

if len(sys.argv) < 2:
    sys.exit('no arguments specified')

for arg in sys.argv [1:]:
    print('Your name is ' , arg)
# try:
#     print('Hello , may name is ' , sys.argv[1])

# except IndexError:
#     print('list index out of range')
