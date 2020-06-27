class Animals:
    feed = 100 #процентов
    instance_ref = []
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animals.instance_ref.append(self)

    def feeding(self, upfeed):
        self.feed += upfeed

class Geese(Animals):
    eggs = 20
    voice = "Га-Га"

    def pick_eggs(self, uneggs):
        self.eggs -= uneggs

class Cows(Animals):
    milk = 100 #процентов
    voice = "Мууу"

    def milking(self, unmilk):
        self.milk -= unmilk
        self.feed -= unmilk / 10


class Sheeps(Animals):
    wool = 100 #процентов
    voice = "Беее"

    def shearing(self, unwool):
        self.wool -= unwool

class Hens(Animals):
    eggs = 20
    voice = "Ко-ко-ко"

    def pick_eggs(self, uneggs):
        self.eggs -= uneggs

class Goats(Animals):
    milk = 100 #процентов
    voice = "Меее"

    def milking(self, unmilk):
        self.milk -= unmilk
        self.feed -= unmilk / 10

class Ducks(Animals):
    eggs = 20
    voice = "Кря-кря"

    def pick_eggs(self, uneggs):
        self.eggs -= uneggs



goose1 = Geese("Серый", 10)
goose2 = Geese("Белый", 8)
cow1 = Cows("Манька", 200)
sheep1 = Sheeps("Барашек", 150)
sheep2 = Sheeps("Кудрявый", 100)
hen1 = Hens("Ко-Ко", 5)
hen2 = Hens("Кукареку", 6)
goat1 = Goats("Рога", 70)
goat2 = Goats("Копыта", 50)
duck1 = Ducks("Краква", 4)
cow1.milking(10)
cow1.milking(10)
cow1.milking(10)
goat1.milking(10)
sheep1.shearing(50)



print(cow1.milk, cow1.feed)
print(goat1.milk)
print(sheep1.wool)
weightsum = sum([x.weight for x in Animals.instance_ref])
print(weightsum)
maxweight = max([x.weight for x in Animals.instance_ref])
print(maxweight)
#print(Animals.__dict__)