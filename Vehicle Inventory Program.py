# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:11:20 2022

@author: wilso
"""

#Class
class Automobile:

    #initialize Class with private variables
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
        
   #Put private variables in public variable to be able to call within class.     
    car =  self.__make = make, self.__model = model, self.__color = color, self.__year = year, self.__mileage = mileage
    
    
    
       
    # Add Vehicle
    def add_vehicle(self):
        if user_input == 1:
         self.__make = str(input('Please enter make of vehicle:'))              
         self.__model = str(input('Please enter model of vehicle:'))
         self.__color = str(input('Please enter color of vehicle:'))
         self.__year = int(input('Please enter year of vehicle:'))
         self.__mileage = int(input('Please enter mileage of vehicle:'))
         vehicles.append(Automobile(make, model, color, year, mileage))
        else:
            return menu()
    
    
    
 
    

   
#empty list to append vehicle to        
vehicles = []


# Menu Function


def menu():
        print("[1] Add a vehicle to inventory")
        print("[2] Delete a Vehicle")
        print("[3] View the list of vehicles")
        print("[0] Exit the program")
 
menu()
option = int(input("Enter your option: "))
user_input = option

while option != 0:
        if option == 1:
            Automobile(make, model, color, year, mileage).add_vehicle(self)
        elif option == 2:
            #do option 2 stuff
            print("Option 2 has been called.")
        elif option == 3:
            #do option 2 stuff
            print("Option 3 has been called.")   
        else:
            print("Invalid option.")
        
        
print()    
menu()
option = int(input("Enter your option: "))

print("Thanks for using this program. Goodbye")
        
        
    
    
