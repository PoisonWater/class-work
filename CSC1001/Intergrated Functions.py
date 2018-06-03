### 切片
L = list(range(101))
L_slice = L[::10] # L[start:end:step]
print(L_slice)

### 迭代
for x,y,z in [(1,1,2),(2,3,5),(3,5,8)]:
    print("{} + {} = {}".format(x,y,z))

### 列表生成式
print([t*t for t in range(1,11)]) # Basic. Result:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([t^2 for t in range(1,11)]) ## What??? Result: [3, 0, 1, 6, 7, 4, 5, 10, 11, 8]

print([x * x for x in range(1, 11) if x % 2 == 0]) # Add if. Result:[4, 16, 36, 64, 100]

print([m + n for m in 'ABC' for n in 'XYZ']) # Double
# Showing all possible results: ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

dictionary = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in dictionary.items()]) # 词典也可使用列表生成器！
# Result: ['y=B', 'x=A', 'z=C']

### 生成器 Generator
generator = (x * x for x in range(4))
print(generator) # Result: <generator object <genexpr> at 0x10463c200> (ID)
# 可认为生成器Generator为 Queue :
print(next(generator)) # 0
print(next(generator)) # 1
print(next(generator)) # 4
print(next(generator)) # 9
# print(next(generator)) # Error.

generator = (x * x for x in range(4))
# 亦可运用 for loop：
for n in generator:
    print(n)

## Eg. Fibonacci Sequence:
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b ## Another method to define Generator.
        a, b = b, a + b
        n = n + 1
    return 'done'

f6 = fib(6)
for i in f6:
    print(i) # Result: 1,1,2,3,5,8

f6 = fib(6)
while True: # Result of this while loop: 
    try:
        print("g :", next(f6))
    except StopIteration as e: # g : 1, g : 1, g : 2, g : 3, g : 5, g : 8, Iteration Done!
        print("Iteration Done!")
        break

## Eg2. 生成器执行顺序的理解：
 # 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
 # 生成器Generator，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1') 
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
print(next(o)) # step1 ; 1
print(next(o)) # step2 ; 3
print(next(o)) # step3 ; 5