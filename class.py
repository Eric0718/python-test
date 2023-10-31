
class Animal:
    name = 'Animal'
    food = 'food'
    age = 1
    def eat(self):
        print("{} eat {}!".format(self.name,self.food))
    def myAge(self):
        print("I'm a/an {},my age is {}.".format(self.name,self.age))
    

class Taiger(Animal):
    def __init__(self,name,food,age):
        self.name = name
        self.food = food
        self.age = age
    def myAge(self):
        print("my age is {}.".format(self.age))

tg = Taiger("cat","lao shu",2)

tg.eat()
tg.myAge()

super(Taiger,tg).eat()
super(Taiger,tg).myAge()
print("super name:%s,food:%s,age:%d." %(super(Taiger,tg).name,
    super(Taiger,tg).food,super(Taiger,tg).age))
