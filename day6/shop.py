
class Customer:
    def __init__(self,name,item,phone):
        self.name=name
        self.item=item
        self.phone=phone
class Order(Customer):
    def Order_details(self,item,order_time,order_id):
        self.item=item
        self.order_time=order_time
        self.order_id=order_id
obj=Order()
obj.Customer("raj","chicken","10002")

        

        