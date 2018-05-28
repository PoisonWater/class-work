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