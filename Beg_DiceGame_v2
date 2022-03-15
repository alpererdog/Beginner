from random import randint
while True:
    try:
        dicefacecount = input('How many faces u want on dice? : ')
        df = int(dicefacecount)
        if df < 2:
            print('You can enter minimum 2 faces for dice!')
            pass
        elif df > 9:
            print('You can enter maximum 9 faces for dice!')
            pass
        else:
            face = randint(1, df)
            while True:
                faceguess = input("Now! Let's give me a number for you! : ")
                fg = int(faceguess)
                dff = df + 1
                if fg < 2:
                    print('Wrong entry! Your guess must be bigger then 2! Try again please!')
                    pass
                elif fg > df:
                    print('Wrong entry! Your guess must be smaller then {}! Try again please!'.format(dff))
                    pass
                elif face == fg:
                    print("Yes! Right guess, inbound face was {}".format(face))
                    break
                else:
                    print('Oh no! Wrong guess, inbound face was {} but your guess is {}.'.format(face, fg))
                    break
    except:
        print('Wrong entry! Try again please!')
        pass
