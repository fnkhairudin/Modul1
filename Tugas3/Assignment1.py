if __name__ == '__main__':
    import string
    alphabet = string.ascii_uppercase + string.ascii_uppercase # supaya ketika index character yg ingin dienkripsikan melebihi 26, maka akan diulang lagi kembali ke character awal, yaitu 'A'
    while True:
        inputMessage = str(input("Input your message:")).upper()
        print('Your message encrypted into:')
        for i in inputMessage:
            if i == ' ':
                print(' ', end='')
            if i == '.': #conditional statement untuk jika terdapat '.' makan outputnya tetap akan '.'
                print('.', end='')
            if i == 'Z':
                print('', end='')
            elif alphabet[alphabet.find(i) + 4] == 'D': #conditional statement untuk jika output 'D', maka akan "di-skip" (continue)
                continue
            print(alphabet[alphabet.find(i) + 4], end='')
        q1 = input('\n\nDo you still want to input another message? (y/n): ')
        if q1 == 'y':
            True
        else:
            print('\n----------See you again!----------')
            break
