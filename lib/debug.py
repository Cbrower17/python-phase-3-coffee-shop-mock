#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    # print("HELLO! :) let's debug")
    c1 = Customer('Steve')
    # c2 = Customer('')
    # c1.name = True
    c1.name = "a"*26
    # ipdb.set_trace()
