class computer:
    def __init__(self):
        self.__mprice=40000

    def sell(self):
        print("Price:", self.__mprice)

    def setmprice(self,p):
        self.__mprice=p


ob=computer()
ob.sell()
ob.__mprice=60000
ob.sell()
ob.setmprice(80000)
ob.sell()