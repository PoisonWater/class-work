def f(x):
    return x * x
inputs = [1,2,3,4,5,6,7,8,9]
# Expected outputs: [1, 4, 9, 16, 25, 36, 49, 64, 81]

## Normal Solution:
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

## Using map():
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

### map()的更多运用：
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))) # return string 的 list
print(type(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))) # <class 'map'>