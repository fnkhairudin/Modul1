if __name__ == '__main__': 
    """String Find-Replace Game!!!"""

    while True:
        text = str(input("Input your string: "))
        oldText = str(input("Input the text that you want to replace: "))
        newText = str(input("The oldText will replaced with: "))

        if oldText not in text:
            print(f'There is no "{oldText}" in "{text}". Try again!')
            continue

        lowest_index = text.find(oldText)
        highest_index = text.find(oldText) + len(oldText)

        print(text[:lowest_index] + newText + text[highest_index:])

        q1 = input('\n\nDo you want to still play Find-Replace game? (y/n): ')
        if q1 == 'y':
            print('\nHave Fun!!!')
        else:
            print('\n----------See you again!----------')
            break
