from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self._name
    def set_name(self, name):
        if( isinstance(name, str) and 0<len(name)<=15):
            self._name = name
        else:
            raise Exception ("hey big no no on that one boss")
    name = property(get_name, set_name)
    def orders(self):
        orders=[]
        for order in Order.all:
            if order.customer == self:
                orders.append(order)
        return orders
    def coffees(self):
        coffees = []
        for order in Order.all:
            if order.customer == self and order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
        
