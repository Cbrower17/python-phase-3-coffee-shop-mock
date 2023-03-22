from classes.order import Order

class Coffee:
    def __init__(self, name):
        if isinstance(name,str):
            self._name = name
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        raise Exception('Cannot change name')
    name = property(get_name, set_name)

    def orders(self):
        orders = []
        for order in Order.all:
            if order.coffee == self:
                orders.append(order)
        return orders
    
    def customers(self):
        customers = []
        for order in Order.all:
            if order.coffee == self and order.customer not in customers:
                customers.append(order.customer)
        return customers
    
    def num_orders(self):
        orders = self.orders()
        return len(orders)
    
    def average_price(self):
        total_price = 0
        number_of_orders = 0 
        for order in Order.all:
            if order.coffee == self:
                total_price += order.price
                number_of_orders += 1
        return (total_price/number_of_orders)
