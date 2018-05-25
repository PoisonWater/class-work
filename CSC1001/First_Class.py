class Flower:
    def __init__(self,name = 'flower',petal = 4,price = 5.0):
        while not name.isalpha():
            name = input('Improper input!The name of flower has to be the string.\nInput here:')
        self.name = name
        while (not petal.isdigit()) or (int(petal) <= 0):
            petal = input('Improper input!The number of petals has to be the integer larger than 0.\nInput here:')
        self.petal = petal
        while (price.isalpha is True) or (type(eval(price)) is int) or (eval(price) <=0):
            price = input('Improper input!The price of flower has to be the float larger than 0.\nInput here:')
        self.price = price

    def setName(self,name):
        while not name.isalpha():
            name = input('Improper input!The name of flower has to be the string.\nInput here:')
        self.name = name

    def setPetal(self,petal):
        while (not petal.isdigit()) or (int(petal) <= 0):
            petal = input('Improper input!The number of petals has to be the integer larger than 0.\nInput here:')
        self.petal = petal

    def setPrice(self,price):
        while (price.isalpha is True) or (type(eval(price)) is int) or (eval(price) <= 0):
            price = input('Improper input!The price of flower has to be the float larger than 0.\nInput here:')  
        self.price = price

    def getName(self):
        print('The name of your flower is',self.name)

    def getPetal(self):
        print('The number of petals is',self.petal)

    def getPrice(self):
        print('The price of flower is',self.price)

def main():
    name = input('please enter the name of the flower:')   
    petal = input('please enter the number of petals:')
    price = input('please enter the price of the flower:')
    myflower = Flower(name,petal,price)

    newName = input('If you want to set a new name for your flower, please enter it here. Otherwise, just kick the key "Enter":')
    if newName != '':
        myflower.setName(newName)

    newPetal = input('If you want to set a new number of petals, please enter it here. Otherwise, just kick the key "Enter":')
    if newPetal != '':
        myflower.setPetal(newPetal)
    
    newPrice = input('If you want to set a new price for your flower, please enter it here. Otherwise, just kick the key "Enter":')
    if newPrice != '':
        myflower.setPrice(newPrice)

    myflower.getName()
    myflower.getPetal()
    myflower.getPrice()
    
main()