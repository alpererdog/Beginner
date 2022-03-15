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
            print('{} is came between {} faces.'.format(face, df))
            break
    except:
        print('Wrong entry! Try again please!')
        pass