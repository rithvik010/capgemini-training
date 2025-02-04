class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    def checking_availability(self,quantity):
        if quantity<=self.stock:
            print("Stock Available")
        else:
            print("Stock Not Available")
product1=Product("Mobile",10000,5)
product1.checking_availability(4)
product1.checking_availability(7)