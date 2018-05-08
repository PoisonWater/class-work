import sys
while True: # offering the opportunity for the user to restart again
    dic , lst , lstVar , guessList = {} , [] , [] , []
    numList = ['7129','4306','9475','2560','6251','5783','0817','1948','3094','2478','3759','0462'] # tested and optimized manually to minimize the trials ( I have designed a ‘for’ loop to examine it can absolutely get the result within the given 11 numbers.)
    print('Initializing...')
    for i in range(123,9877):
        switch = 0
        istr = str(i)
        if len(istr) == 3:
            istr = '0' + istr
        for s in range(0,4):
            ilist = istr
            ilist.split()
            if ilist.count(istr[s]) >1 :
                switch += 1
        if switch != 0:
            continue
        lst.append(istr) # By using a for loop to add a ‘0’ ahead all the three digit numbers, such as ‘123’, and then put all the capable numbers in a list.

#The following until line 37 shows all the possible outcomes of the 5040 numbers as lists of tuples and then append the list (as value) into the dictionary named after ‘dic’, while each key is a possible number in numList.
    for istr in lst:
        ilist , lstVar = [] , []
        for b in istr:
            ilist.append(b)
        for t in range(0,12):
            cor , exa = 0 , 0
            numListStr = numList[t]
            guess = []
            for b in numListStr:
                guess.append(b)
            for s in range(0,4):
                if ilist[s] == guess[s]:
                    exa += 1
                if guess[s] in ilist:
                    cor += 1
            lstVar.append((cor,exa))
        dic[istr] = lstVar

    print('\nThis program is designed to guess a FOUR digit number with no repeated digits.\nSo, choose a “secret number” with no repeated digits and have it written down to let me guess.\n\nAlso, you need to give me two pieces of information about my guess number compared with your secret number after each guess.\nOne is how many digits in my guess numbers are in your secret number, and we call them to be \'Correct\'.\nThe other is how many digits in my guess numbers are exactly in the same place as your secret number, and we call them to be \'Exact\'\n\nIf you want to quit this program in the middle of the process, just enter x and I will let you go.')
    egJudge = input('\nIf you still cannot understand what you need to do, enter SOS below, and the GREAT Anderson will help you out.\nBut if you are an old driver, knowing what you need to do, just press enter to play.\n')
    if egJudge == 'SOS':
        print('\nFor instances, say the chosen secret number is “2468”, the following table shows the feedback as a result of each guess provided by the game-player:')
        print('Guess  Correct  Exact   Remark'+'\n'+'1357      0       0     None of the digits (1,3,5 & 7) are from 2468'+'\n'+'2890      2       1     Only digits 2 & 8 appear in 2468 and digit 2 is in the exact position'+'\n'+'8294      3       0     Only digits 2, 4 & 8 appear in 2468 and none of 3 digits appear in the exact position'+'\n'+'2486      4       2     All digits from “guess” also from 2468 and only digits 2 & 4 appear in the exact position'+'\n'+'2468      4       4     Guess matches secret number')
        input('You must be fully awared of the things you need to do. So press Enter and let the journey begin!\n')
    elif egJudge == 'x':
        sys.exit()

    #The following is designed to give the user correct outputs and let them give the system their feedbacks.
    for i in range(0,12):
        if len(dic) <= 1:
            continue # Jump through the rest of the for loop between line 41-69 when the output of the results is only one or none
        print('\nGuess '+str(i+1)+'/11: '+numList[i])
        co = input('How many correct digits are there?\nEnter here: ')
        if co == 'x':
            sys.exit()
        while (not co.isdigit()) or int(co) > 4 or int(co) < 0: # Assure the input is in correct form and the program won’t return error.
            co = input('Wrong input! How many correct digits are there?\nEnter here again: ')
            if co == 'x':
                sys.exit()
        cor = int(co)
        if cor != 0 :
            ex = input('How many exact digits are there?\nEnter here: ')
            if ex == 'x':
                sys.exit()
            while (not ex.isdigit()) or int(ex) > cor or int(ex) < 0:
                ex = input('Wrong input! How many exact digits are there?\nEnter here: ')
                if ex == 'x':
                    sys.exit()
            exa = int(ex)
        elif cor == 0:
            exa = 0
        guessList.append('Guess '+str(i+1)+'/11: '+numList[i]+' | Correct:'+co+' Exact:'+str(exa)) # Saving the guess histories and feedbacks
        for guesses in guessList:
            print(guesses) # Showing the histories and feedbacks after each input of feedbacks.
        for lstr in lst:
            if lstr in dic:
                varList = dic[lstr]
                if varList[i] != (cor,exa):
                    del dic[lstr] # Delete the inappropriate elements from the dictionary.

    # Judges whether the result is appropriate and give the corresponding results:
    if len(dic) == 0:
        print('You must be kidding! No 4-digit number can satisfy your description! Let us start again!')
        condition = input('Press enter to restart. Press x to quit\n')
        if condition == 'x':
            sys.exit()
    else:
        print('It must be '+str(dic.keys()).strip('dict_keys([\'').strip('\'])')+'.\nCongratulations to me! ;)')
        condition = input('Press enter to restart. Press x to quit.\n')
        if condition == 'x':
            sys.exit()