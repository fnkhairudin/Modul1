if __name__ == '__main__':
    while True:
        print('-------------------------Collatz Sequence-------------------------\n')
        n = int(input('Enter your starting number: '))
        if n == 1 or n == 0:
            print('try another number, please! Or you will get infite looping!!!\n')
            continue
        print(f'{n}, ', end='')
        while n != 1:
            if n%2 == 0:
                n = n/2
            else:
                n = n*3+1
            print(f'{int(n)}, ', end='')
        q1 = input('\nDo you want to play this game again? (y/n): ')
        if q1 == 'y':
            print('okey lets do it! Enter you starting number again!\n')
        else:
            print('\nsee you again!')
            break
