import vector
import time
f = open('training.txt')
text = f.read()
f.close()
lines = text.split('\n')
f = open('testing.txt')
test = f.read()
f.close()
test = test.split('\n')

dataTraining = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : []}
dataTesting = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : []}

### Training Session ###

print('\nBeginning of Training @',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print('----------------------------------------')
print('             Training Info')
print('----------------------------------------')
handwritten = ''
## Fulfill the dataTraining dict
for line in lines:
    if ' ' in line:
        templist = []
        for letter in handwritten:
            templist.append(int(letter))
        this_tuple = tuple(templist)
        dataTraining[int(line[1])].append(this_tuple)
        handwritten = ''
    else:
        handwritten = handwritten + line
totalSamples = 0
for i in range(10):
    t = len(dataTraining[i])
    print('               ',i,'=',str(t).rjust(3))
    totalSamples += t
print('----------------------------------------')
print('          Total Samples =',totalSamples)
print('----------------------------------------')

### Testing Session ###

print('----------------------------------------')
print('             Testing Info')
print('----------------------------------------')

# define a function to match the first k closest nums
def match(my_tuple,k = 1):
    global dataTraining
    baseData = [] # Fill list with vector distances and nums
    numList = []
    for i in range(10):
        for samp_tuple in dataTraining[i]:
            distance = vector.squared_distance(my_tuple, samp_tuple)
            baseData.append((distance,i))
        baseData.sort()
    for i in range(k):
        numList.append(baseData[i][1])
    return mode(numList)

# define a function to get the mode of the list
def mode(L):
    elementdict = {}
    for i in L:
        if i in elementdict:
            elementdict[i] += 1
        else:
            elementdict[i] = 1
    return sorted(elementdict.items(),key = lambda x:x[1],reverse = True)[0][0]

# Infos from testing.txt
handwritten2 = ''
for line in test:
    if ' ' in line:
        templist = []
        for letter in handwritten2:
            templist.append(int(letter))
        test_tuple = tuple(templist)
        dataTesting[int(line[1])].append(test_tuple)
        handwritten2 = ''
    else:
        handwritten2 = handwritten2 + line

def checktest():
    guesses, guessW = 0,0
    ### results of test.txt's guesses, inside each list, there are two elements reperesenting corrects and all guesses.
    guessResults = {0 : [0,0], 1 : [0,0], 2 : [0,0], 3 : [0,0], 4 : [0,0], 5 : [0,0], 6 : [0,0], 7 : [0,0], 8 : [0,0], 9 : [0,0]}
    for num in range(10):
        for test_tuple in dataTesting[num]:
            guessNum = match(test_tuple)
            if num != guessNum:
                guessResults[num][0] += 1
                guessW += 1 
            guessResults[num][1] += 1    
            guesses += 1
    for i in range(10):
        print('           ',i,'=',str(guessResults[i][1]).rjust(3),',',str(round(100*(1-guessResults[i][0]/guessResults[i][1]))).rjust(3),end = '')
        print('%')
    print('----------------------------------------')
    print('          Accuracy = ',round(100-100*guessW/guesses,4),'%',sep = '')
    print('        Correct/Total = ',guesses - guessW,'/',guesses,sep = '')
    print('----------------------------------------')
checktest()
print('End of Training @',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

### Predict Session ###
f = open('predict.txt')
pre = f.read()
f.close()
pre = pre.split('\n')
handwritten3 = ''
tlist = []
for pres in pre:
    if ' ' in pres:
        for i in handwritten3:
            tlist.append(int(i))
        print(match(tuple(tlist)))
        tlist = []
        handwritten3 = ''
    else:
        handwritten3 = handwritten3 + pres