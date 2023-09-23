#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name= "Snoopy", breed = "Mastiff" ):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (isinstance(name, str)) and 0 < len(name)<= 25:
            self._name = name
            # print(f"My name is {self._name}")
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
            return self._breed
            # print(f"{self._breed}")
        else:
            print("Breed must be in list of approved breeds." )

    breed = property(get_breed, set_breed)
            
           
    
        

snoopy = Dog("Snoopy")
snoopy.set_name(" ")


    

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self._age = 0
#     def get_age(self):
#         print(self._age)
#     def set_age(self,age):
#         if isinstance(age, int) and 0<age<=20:
#             self._age = age
#             print(f"I am {self._age} years old")
#         else:
#             print(f"Age should be an integer between 0 and 20 years")
#     age = property(get_age, set_age)

# snoopy = Dog("Snoopy", "Chihuahua")
# snoopy.set_age(1)
# snoopy.get_age()
# print(snoopy.name)
# print(snoopy.breed)