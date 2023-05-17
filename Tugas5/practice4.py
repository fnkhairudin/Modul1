if __name__ == '__main__':
    import sys

    ticDict = {
        'top-l':' ',
        'top-m':' ',
        'top-r':' ',
        
        'mid-l':' ',
        'mid-m':' ',
        'mid-r':' ',

        'low-l':' ',
        'low-m':' ',
        'low-r':' '
    }

    def tictacMain():
        print("""
        1. Play Game
        2. Exit
            """)
        userInput = int(input("Play Game (1) or Exit (2): "))
        if userInput == 1:
            movePlayer(ticDict)
        else:
            sys.exit()


    def playerX(dict1):
        #valuesInputX = str(input("which space do you want to choose (Player X): ")) 
        while True:
            valuesInputX = str(input("which space do you want to choose (Player X): ")) #top-l
            if valuesInputX in dict1: # keys 'top-l' in ticDict
                if ticDict[valuesInputX] != ' ': # mengecek apakah dalam kotak tersebut sudah terisi
                    print('Check your move!')
                else:
                    dict1[valuesInputX] = 'X' #ticDict['top-l'] = X ## diganti 'X'
                    printBoard(dict1)
                    break               
            else:
                print('Try another move!')


    def playerO(dict1):
            #valuesInputO = str(input("which space do you want to choose (Player O): "))
            while True:
                valuesInputO = str(input("which space do you want to choose (Player O): "))
                if valuesInputO in dict1: # keys 'top-m' in ticDict ## misal 'top-m'
                    if dict1[valuesInputO] != ' ': # mengecek apakah dalam kotak tersebut sudah terisi
                        print('Check your move!')
                    else:
                        dict1[valuesInputO] = 'O' #ticDict['top-m'] = 'O' ## diganti 'O'
                        printBoard(dict1)
                        break
                else:
                    print('Try another move!')


    def movePlayer(dict1):
        print("""
        ENJOYYYY!!!
        """)
    # player movement    
        while True:
            # player X
            playerX(ticDict)
            if ' ' not in dict1.values():
                print('Finished!!')
                break

            # player O
            playerO(ticDict)    
            if ' ' not in dict1.values():
                print('Finished!!')
                break


    def printBoard(dict1):      
        #board
        print(dict1['top-l'] + '|' + dict1['top-m'] + '|' + dict1['top-r'])
        print('-+-+-')
        print(dict1['mid-l'] + '|' + dict1['mid-m'] + '|' + dict1['mid-r'])
        print('-+-+-')
        print(dict1['low-l'] + '|' + dict1['low-m'] + '|' + dict1['low-r'])
