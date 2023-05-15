if __name__ == '__main__':
    """input the message argument in string type"""
    def encryptor(message):
        inputMessage = message.upper()    
        import string
        alphabet = string.ascii_uppercase*2 # supaya ketika index character yg ingin dienkripsikan melebihi 26, maka akan diulang lagi kembali ke character awal, yaitu mulai dari 'A'
        while True:
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
            break
