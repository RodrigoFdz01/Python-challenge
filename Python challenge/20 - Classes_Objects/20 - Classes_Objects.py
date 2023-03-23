#Creating a Class
#To create a class we need the key word class followed by the name and colon. Class name should be CamelCase.
class Person:
  pass
print(Person)



#Creating an Object
#We can create an object by calling the class.
p = Person()
print(p)



class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)


class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


#Object Methods
#Objects can have methods. The methods are functions which belong to the object.


class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())



# Object Default Methods
# Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:


class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())


# Herencia
# Usando la herencia podemos reutilizar el código de la clase principal. La herencia nos permite definir una clase que hereda todos los métodos y propiedades de la clase padre. La clase padre o superclase o clase base es la clase que proporciona todos los métodos y propiedades. La clase secundaria es la clase que hereda de otra clase principal. Vamos a crear una clase de estudiante heredando de la clase de persona.

class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# No llamamos al constructor init () en la clase secundaria.
#  Si no lo llamamos, aún podemos acceder a todas las propiedades desde el padre. 
# Pero si llamamos al constructor, podemos acceder a las propiedades principales llamando a super .
# Podemos agregar un nuevo método al elemento secundario o podemos anular los métodos de la clase principal 
# creando el mismo nombre de método en la clase secundaria. Cuando agregamos la función init (),
#  la clase secundaria ya no heredará la función init () de los padres.

