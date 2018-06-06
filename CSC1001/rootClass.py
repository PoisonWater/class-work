a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

class Root:
    def Root(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def getRoot1(self):
        delta = b**2 - 4*a*c
        rdelta = delta ** 0.5
        root1 = (-b+rdelta)/2/a
        return root1

    def getRoot2(self):
        delta = b**2 - 4*a*c
        rdelta = delta ** 0.5
        root2 = (-b-rdelta)/2/a 
        return root2

first = Root(a,b,c).getRoot1()
second = Root(a,b,c).getRoot2()