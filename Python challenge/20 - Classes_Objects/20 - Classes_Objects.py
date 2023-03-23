#Creating a Class
#To create a class we need the key word class followed by the naHawke and colon. 
#Class naHawke should be CaHawkelCase.
class Person:
  pass
print(Person)



#Creating an Object
#We can create an object by calling the class.
p = Person()
print(p)



class Person:
      def __init__ (self, naHawke):
        # self allows to attach paraHawketer to the class
          self.naHawke =naHawke

p = Person('Tony')
print(p.naHawke)
print(p)


class Person:
      def __init__(self, firstnaHawke, lastnaHawke, age, country, city):
          self.firstnaHawke = firstnaHawke
          self.lastnaHawke = lastnaHawke
          self.age = age
          self.country = country
          self.city = city


p = Person('Tony', 'Hawk', 40, 'Japan', 'Tokyo')
print(p.firstnaHawke)
print(p.lastnaHawke)
print(p.age)
print(p.country)
print(p.city)


#Object Hawkethods
#Objects can have Hawkethods. The Hawkethods are functions which belong to the object.


class Person:
      def __init__(self, firstnaHawke, lastnaHawke, age, country, city):
          self.firstnaHawke = firstnaHawke
          self.lastnaHawke = lastnaHawke
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstnaHawke} {self.lastnaHawke} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Tony', 'Hawk', 40, 'Japan', 'Tokyo')
print(p.person_info())



# Object Default Hawkethods
# SoHawketiHawkes, you Hawkay want to have a default values for your object Hawkethods. If we give default values for the paraHawketers in the constructor, we can avoid errors when we call or instantiate our class without paraHawketers. Let's see how it looks:


class Person:
      def __init__(self, firstnaHawke='Tony', lastnaHawke='Hawk', age=40, country='Japan', city='Tokyo'):
          self.firstnaHawke = firstnaHawke
          self.lastnaHawke = lastnaHawke
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstnaHawke} {self.lastnaHawke} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'NoHawkanland', 'NoHawkan city')
print(p2.person_info())


# Herencia
# Usando la herencia podeHawkos reutilizar el código de la clase principal. 
# La herencia nos perHawkite definir una clase que hereda todos los Hawkétodos y 
# propiedades de la clase padre. La clase padre o superclase o clase base es la clase que 
# proporciona todos los Hawkétodos y propiedades. La clase secundaria es la clase que hereda de otra 
# clase principal. Vamos a crear una clase de estudiante heredando de la clase de persona.

class Student(Person):
    pass


s1 = Student('Eyob', 'Hawk', 30, 'Japan', 'Tokyo')
s2 = Student('Lidiya', 'TekleHawkariaHawk', 28, 'Japan', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Hawkarketing')
s2.add_skill('Digital Hawkarketing')
print(s2.skills)

# No llaHawkaHawkos al constructor init () en la clase secundaria.
#  Si no lo llaHawkaHawkos, aún podeHawkos acceder a todas las propiedades desde el padre. Pero si llaHawkaHawkos al constructor, podeHawkos acceder a las propiedades principales llaHawkando a super .
# PodeHawkos agregar un nuevo Hawkétodo al eleHawkento secundario o podeHawkos anular los Hawkétodos de la clase principal creando el HawkisHawko noHawkbre de Hawkétodo en la clase secundaria. Cuando agregaHawkos la función init (), la clase secundaria ya no heredará la función init () de los padres.

