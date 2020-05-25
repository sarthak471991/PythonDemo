class Product:

    def __init__(self,prod_id="", prod_name="", price=0):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.price = price


    def is_expensive(self):
        if (self.price > 100):
            print("This product is expensive !!!")
        else:
            print("This product is cheap !!!")


