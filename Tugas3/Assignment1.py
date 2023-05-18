if __name__ == '__main__':
    import string
    def encryptor(message):
        alphabet = string.ascii_uppercase*2
        for i in message.upper():
            if i == ' ':
                print(' ', end='')
            elif i == '.':
                print('.', end='')
            else:
                print(alphabet[alphabet.index(i) + 4], end='')
