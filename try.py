def main():
    x = get_int()
    print('x is : ', x)


def get_int():
    while True:
        try:
            return int(input('what is the value of x ? '))

        except ValueError:
            # print('your x is not a number')
            pass




main()
