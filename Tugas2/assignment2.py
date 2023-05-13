if __name__ == '__main__':
    while True:
        print('\n---------------Collatz Sequence---------------')
        n = int(input('Enter your starting number: '))
        if n == 1 or n == 0:
            print('try another number, please! Or you will get infite looping!!!')
            continue
        print(f'{n}, ', end='')
        while n != 1:
            if n%2 == 0:
                n = n/2
            else:
                n = n*3+1
            print(f'{int(n)}, ', end='')
        ask2 = input('\nDo you want to play this game again? (y/n): ')
        if ask2 == 'y':
            print('okey lets do it! Enter you starting number again!')
        else:
            print('\nsee you again!')
            break
