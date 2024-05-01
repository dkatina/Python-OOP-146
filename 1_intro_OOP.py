#Object Oriented Programing (OOP) : The concept of creating blueprint (classes) 
#to help us mass produce objects with simialr attributes and functionalities

#define a class (Blueprints)
class Vehicle(): #PascaleCase
    pass #no features....yet


#creating objects or an instance of the class

car = Vehicle() #set variable equal to the class: DONT FORGET PARENS
truck = Vehicle()
print(car)
print(truck)

#now car, is able to do all the things a vehicle can (nothing yet)


#Why?
#-- Modularity: Allows further organization
#-- Reuse: Pnce we build a class, we can continue to reuse it create mass amounts of objects
#-- Scalability: By reusing our code we are able to scale our applications further
#-- Maintenance: Update specific instances rather than the whole codebase



#======== Attributes ==========

#attributes are the qualities our objects will have (object variables)

#-------- Class Attributes ---------
#These are characteristics that every instance of the class will share

class Vehicle():
    wheels = 4
    engine = 'V8'
    seats = 5


car = Vehicle()
truck = Vehicle()
mini_van = Vehicle()

#accessing attributes => instance.attribute
print('\ncar')
print(car.engine)


print('\nTruck')
print(truck.engine)

print('\nMini Van')
print(mini_van.seats)


#-------- Instance Attributes -------------

#These are the attributes that may differ between instances of the same class,
#allow for our class to produce more flexible objects

#__init__: this is our constructor, a function whos job it is to instantiate our
#new object (set the attributes passed in as arguments on the new object)


class Vehicle():
    wheels = 4 #class attribute (something all vehicles get)

    def __init__(self, color, engine, seats): #instance attributes (things that can be different between vehicles)
        self.color = color
        self.engine = engine
        self.seats = seats

#self is a key word to tell the class what instance we are currently working on


#creating objects with instance attributes

#object = Class(instance_attributes)
car = Vehicle('red', 'V12', 2)

#The Instanciating Sequence
#-- car object gets created
#-- __init__ constructor method gets called automatically on the new object (self)
#-- adds the arguments to the car as attributes.

print('---------custom instances------')
print(car.color)
print(car.engine)
print(car.wheels)


truck = Vehicle('Black', 'V8', 5)
mini_van = Vehicle('Silver', 'V6', 8)

print(truck.engine)
print(mini_van.seats)


#--------Changing Attributes -------

#object.attribute = new_value
print('\nPainting my car green')
car.color = 'green'
print(car.color)


#increment attributes
print('\nExtend my van to have another bench')
mini_van.seats += 3
print(mini_van.seats)





#============= Methods =========================


#methods are class functions, that can only be called on instances of that class

#---common methods----
#- get object info
#- changing attributes
#- incrementing object atts
#- adding to objects atts (appending to a object list)



class Vehicle():
    wheels = 4 #class attribute (something all vehicles get)

    def __init__(self, color, engine, seats): #instance attributes (things that can be different between vehicles)
        self.color = color
        self.engine = engine
        self.seats = seats

    #methods start here

    def get_info(self):
        print(f'This is a {self.color} vehicle with a {self.engine} engine, and {self.seats} seats.')

    
    def paint_vehicle(self, new_color):
        print(f'Painting the vehicle from {self.color} to {new_color}!')
        self.color = new_color


royce = Vehicle(seats=5, color='Black', engine='V12')
joe_da_tessy = Vehicle(seats=7, color='Chrome', engine='electric')


#calling methods: instance.method()
royce.get_info()
joe_da_tessy.get_info()

#call our paint_vehicle Method

royce.paint_vehicle('Pearl White')
print(royce.color)


