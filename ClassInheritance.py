class Fan:
    def __init__(self,name,color,price):
        self.__name = name
        self.__color = color
        self._price = price
    def printname(self):
        return "Name : " + self.__name + " Color : " + self.__color + " Price : " + str(self._price)


class Khaitan(Fan):
    def __init__(self,name,color,price):
        super().__init__(name,color,price)
    def isavailable(self):
        if self._price < 1500:
            return "Not Available"
        else:
            return "Available"
class Usha(Fan):
    def __init__(self,name,color,price):
        super().__init__(name,color,price)
    def isavailable(self):
        if self._price < 2000:
            return "Not Available"
        else:
            return "Available"


kf = Khaitan("KF1", "blue",1600)
kf.price = 500
print(kf.printname())
print(kf.isavailable())

f1 = Fan("F1", "blue",1600)
f1.price = 400
print(f1.printname())