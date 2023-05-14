class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        print(self.name + ' ' + 'is walking')
    def speak(self):
        print (' Hello my name is ' + ' ' + self.name + ' ' + 'and i am' + ' ' + str(self.age ) + ' '+ 'years old')
    def eat(self):
        print(self.name +' '+  'is eating...')
        


jose = Person('jose', 22)
jose.walk()
jose.speak()
jose.eat()
print('--------------------------')
maria = Person('maria', 18)
maria.speak()
maria.walk()
maria.eat()
print(maria.name + ' =' + str(maria.age))
