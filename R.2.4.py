class Flower:
    def __init__(self, type_of_flower="", number_of_petals=0, price_of_flower=0.00):
        self.type_of_flower = type_of_flower
        self.number_of_petals = number_of_petals
        self.price_of_flower = price_of_flower

    def get_type(self):
        return self.type_of_flower
    
    def get_number_of_petals(self):
        return self.number_of_petals
    
    def get_cost(self):
        return self.price_of_flower


flower = Flower('Rose', 20, 2.50)
print(flower.get_number_of_petals)