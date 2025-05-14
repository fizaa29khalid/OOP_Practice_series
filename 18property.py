class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        """Getter for price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

# Example usage
item = Product(100)

print("Initial Price:", item.price)   # Calls getter

item.price = 150                     # Calls setter
print("Updated Price:", item.price)

item.price = -50                     # Try to set invalid price

del item.price                       # Calls deleter

# Trying to access after deletion will raise an AttributeError
try:
    print(item.price)
except AttributeError:
    print("Price attribute has been deleted.")
