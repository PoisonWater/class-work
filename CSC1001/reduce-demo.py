from functools import reduce
def writeTogether(a,b): # 将字符串合二为一的方法
    return a + b

### reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

### reduce: 将二元函数扩展到多元
print(reduce(writeTogether,["Pan","dora"," ","is"," ","good","!"])) # Result: Pandora is good!
# 运行前提：return值的格式可满足函数的input值
# reduce & map 可运用任何能切片的输入：string list tuple map

### Eg1: Str --> Int
digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
string = "12345678"
def twoDigits(a,b):
    return 10 * a + b
def dig2num(digit):
    return digits[digit]
def str2num(s):
    return reduce(twoDigits,map(dig2num, string))
result1 = str2num(string)
print(type(result1),":",result1)

### Eg2: 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
Dic = {"A":'a',"B":'b',"C":"c",'D':"d",'E':"e",'F':"f",'G':'g','H':"h","P":'p',"L":'l',"O":'o',"L":'l',}
Dic2 = {"a":'A',"b":'B',"c":"C",'d':"D",'e':"E",'f':"F",'g':'G','h':"H"}
def normalize(names):
    def low(n1):
        if n1 in Dic.keys():
            return Dic[n1]
        else:
            return n1
    def capital(word):
        word = Dic2[word[0]]+ word[1:]
        return word
    def getStr(word):
        return reduce(writeTogether,map(low,word))
    def getList(name0):
        return list(map(getStr,name0))
    return list(map(capital,getList(names)))

print(normalize(['ApplE','gooGLE',"bigDAD"]))