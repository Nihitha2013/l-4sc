class c1:
    __p=30
    def __f1(self):
        print("Inside private function")
        

    def f2(self):
        print("Public function")
        print(self.__p)

ob=c1()

ob.f2()

ob.__f1()
print(ob.__p)