# Importing the required libraries
from Entities.Student import *
from Entities.HOD import *
from Entities.Teacher import *
from Database import *
from pwinput import pwinput
import os

# The main menu is displayed here
def main_menu():
    pass
        
        

try: 
    main_menu()
except:
    print("An error occured, try again.")
    main_menu()
    
