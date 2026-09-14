#!/usr/bin/env python3
class Coffee:
    # Create a coffee with a size and price
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # Get the coffee size
    @property
    def size(self):
        return self._size

    # Make sure coffee size is valid
    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Add a one-unit tip to the coffee price
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1