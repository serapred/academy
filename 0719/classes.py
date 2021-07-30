"""
# Rocket Methods
- Start with a copy of the Rocket class, either one you made from a previous exercise
- Add a new method to the class. This is probably a little more challenging than adding attributes, but give it a try.
    - Think of what rockets do, and make a very simple version of that behavior using print statements. For example, rockets lift off when they are launched. You could make a method called *launch()*, and all it would do is print a statement such as "The rocket has lifted off!" If your rocket has a name, this sentence could be more descriptive.
    - You could make a very simple *land_rocket()* method that simply sets the x and y values of the rocket back to 0. Print the position before and after calling the *land_rocket()* method to make sure your method is doing what it's supposed to.
    - If you enjoy working with math, you could implement a *safety_check()* method. This method would take in another rocket object, and call the get_distance() method on that rocket.
"""

from random import randint as rand


def manhattan(p1, p2):
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


def euclidean(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**.5


class Rocket(object):
    """docstring for Rocket"""
    distance = euclidean
    init_trust = 10
    safe_dist = 15

    def __init__(self, x, y):
        super(Rocket, self).__init__()
        self.x = x
        self.y = y

    def get_distance(self, rocket):
        return self.distance(self, rocket)

    def launch(self):
        self.y += rand(1, self.init_trust)
        self.x += rand(1, self.init_trust)

    def land(self):
        self.y = 0

    def safety(self, rocket):
        return self.get_distance(rocket) < self.safe_dist


"""
- Modeling a car is another classic exercise.
    - Define a Car() class.
    - In the __init__() function, define several attributes of a car. Some good attributes to consider are make (Subaru, Audi, Volvo...), model (Outback, allroad, C30), year, num_doors, owner, or any other aspect of a car you care to include in your class.
    - Write one method. This could be something such as *describe_car()*. This method could print a series of statements that describe the car, using the information that is stored in the attributes. You could also write a method that adds km to the mileage of the car.
    - Create a car object, and use your method.
    - Create several car objects with different values for the attributes. Use your method on several of your cars.
"""


class Car(object):
    """docstring for Car"""
    num_wheels = 4

    def __init__(self, make, model, color, fuel_type, year, num_doors, dealer=None, owner=None):
        super(Car, self).__init__()
        self.make = make
        self.model = model
        self.color = color
        self.fuel_type = fuel_type
        self.year = year
        self.num_doors = num_doors
        self.dealer = dealer
        self.owner = owner

    def info(self):
        print(self.__dict__)


from datetime import date
from hashlib import sha1


class Person(object):
    """docstring for Person"""

    def __init__(self, name, surname, birth):
        self.name = name
        self.surname = surname
        self.birth = birth

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @property
    def age(self):
        return date.today().year - self.birth.year


"""
#### Student Class
- Start with your program from Person Class
- Make a new class called Student that inherits from Person.
- Define some attributes that a student has, which other people don't have.
    - A student has a school they are associated with, an university, a course, and other particular attributes.
    - Add a method with the new presentation
- Create a Student object, and prove that you have used inheritance correctly.
    - Set some attribute values for the student, that are only coded in the Person class.
    - Set some attribute values for the student, that are only coded in the Student class.
    - Print the values for all of these attributes.
"""


class Student(Person):
    """docstring for Student"""

    hashing = sha1

    def __init__(self, name, surname, birth, university):
        super(Student, self).__init__(name, surname, birth)
        self.university = university

    def id(self):

        return None  # hashed string of name, surname, birth


if __name__ == '__main__':

    p = Student('Sergio', 'Apreda', date(1992, 2, 26))

    print(f'{p.fullname} {p.age}')
