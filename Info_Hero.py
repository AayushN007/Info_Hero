class Hero:
    
    def __init__(self):
        self.name = "AA"
        self.age = 40
        self.add = "hydrabad"
        self.movies = 20
        
    def act(self):
        print("Hero is acting")
        
    def fight(self):class Hero:
    
    def __init__(self):
        self.name = "AA"
        self.age = 40
        self.add = "hydrabad"
        self.movies = 20
        
    def act(self):
        print("Hero is acting")
        
    def fight(self):
        print("Hero is fightinh")
        
h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.add)
print(h1.movies)

h1.age = 41
h1.movies = 21

h1.mob = 1234567890
h1.awards = 5

h2 = h1
h3 = h2

print(h3.name)
print(h2.age)
print(h1.add)
print(h3.movies)
print(h2.mob)
print(h1.awards)

h3.act()
h2.fight()
        print("Hero is fightinh")
        
h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.add)
print(h1.movies)

h1.age = 41
h1.movies = 21

h1.mob = 1234567890
h1.awards = 5

h2 = h1
h3 = h2

print(h3.name)
print(h2.age)
print(h1.add)
print(h3.mob)
print(h2.awards)

h3.act()
h2.fight()
