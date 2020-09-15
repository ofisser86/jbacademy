# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, city):
        return "The {name} has sailed for {city}!".format(name=self.name, city=city)


black_pearl = Ship("Black Pearl", 800)
dest_city = input()
print(black_pearl.sail(dest_city))
