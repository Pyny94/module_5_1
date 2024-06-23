class HOUSE:
    def __init__(self, name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def to_go(self,new_floor):
        self.new_floor = new_floor
        if 1 > new_floor or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)

h1 = HOUSE('ЖК Горский', 18)
h2 = HOUSE('Домик в деревне', 2)
h1.to_go(24)
h2.to_go(2)


