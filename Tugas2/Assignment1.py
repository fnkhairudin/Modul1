if __name__ == '__main__':
    while True:
        """Fizz Buzz Game"""
        number_input = int(input("input your number: "))
        for i in range(1, number_input+1):
            if i%3 == 0 and i%5 == 0:
                print('FizzBuzz', end=' ')
                continue
            if i%3 == 0:
                print('Fizz', end=' ')
                continue
            if i%5 == 0:
                print('Buzz', end=' ')
                continue
            print(i, end= ' ')
        q1 = input('\n\nDo you want to still try another number (y/n): ')
        if q1 == 'y':
            print('\nHave Fun!!!')
        else:
            print('----------See you again!----------')
            break
