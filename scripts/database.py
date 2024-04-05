# Importing the required libraries
import csv
import datetime
import os
from book import *

class Database:
    # Intilizing the Database Object (Null in this case)
    def __init__(self):
        pass

    """Student Utils"""
    def student_login(self, id, password):
        with open('../data/students.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        