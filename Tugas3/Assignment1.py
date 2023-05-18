if __name__ == '__main__':
    import string
    def encryptor(message):
        print('Your message has been encrypted into:')
        alphabet = string.ascii_uppercase
        for i in message.upper():
            if i == ' ':
                print(' ', end='')
            elif i == '.':
                print('.', end='')
            else:
                print(alphabet[(alphabet.index(i) + 27)%len(alphabet)], end='') # len(alphabet) = 26, supaya ketika key melebihi len(alphabet), maka indexing akan kembali mulai dari index[0] lagi
