
class Order:
    all = []
    def __init__(self,customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    def get_price(self):
        return self._price
    def set_price(self,price):
        if isinstance(price, int) and 0<price<=10:
            self._price = price
        else:
            raise Exception ("nerd")
    price = property(get_price, set_price)
    def get_customer(self):
        return self._customer
    def set_customer(self,customer):
        from .customer import Customer
        if isinstance(customer,Customer):
            self._customer = customer
        
    customer = property(get_customer, set_customer)

    
