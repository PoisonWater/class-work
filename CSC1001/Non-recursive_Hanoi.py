key = 0
n = int(input("Input the size of Hanoi Tower that you want: "))
ranges = [['A','C','B'],['A','B','C']]
moves = [None]*(2**n-1)
t = list(range(1,2**n))

while 1 in t:
    p = 0
    for i in t:
        if i /(2**(n-key-1)) == i // (2**(n-key-1)):
            t[i-1] = -0.01
            moves[i-1] = ranges[key%2][p%3] + ranges[key%2][(p+1)%3]
            p += 1
    key += 1

for move in moves:
    print(move[0],'-->',move[1])