# ДЗ модуль 5_1. "Атрибуты и методы объекта."
# ============================================
class House:       #('ЖК Эльбрус', 30)
    pass
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors
    def go_to (self,new_floor):
        self.new_floor=new_floor
h1 = House('ЖК Горский',18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(h1.name,h1.number_of_floors)
print(h2.name,h2.number_of_floors)
print(h1.new_floor)
print(h2.new_floor)