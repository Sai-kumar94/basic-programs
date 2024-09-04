from dataclasses import dataclass

@dataclass
class Product:
    name:str
    price:float
    quantity:int = 0

    def total_cost(self):
        return self.price*self.quantity
p1=Product(name='laptop',price=1000.0,quantity=3)
p2=Product(name='laptop',price=1000.0,quantity=3)
p3=Product(name='smart laptop',price=3000.0,quantity=2)
print(p1)
print(p1.total_cost())
print(p1==p2)
