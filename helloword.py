# print ("This is great")
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
# full_name = first_name + " " + last_name
# print("Hello " + first_name.capitalize() + " " + last_name.capitalize() + " how are you doing?")
# print(full_name.capitalize())
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.count('i'))

# output = "Hello, " + first_name.capitalize() + " " + last_name.capitalize()
# print(output)
# output = "Hello, {} {}".format(first_name.capitalize(), last_name.capitalize())
# print(output)
# output = "Hello, {0} {1}".format(first_name, last_name)
# print(output)
# output = "Hello, {1}, {0}".format(first_name.capitalize(), last_name.capitalize())
# print(output)
# output = f"Hello, {first_name.capitalize()} {last_name.capitalize()}"
# print(output)
# x = 42 + 399
# print (x)
# print("Performing division")
# y = 2 / 3
# print (y)
# print("Math is complete")
# pi = 3.14159
# print("pi = " + str(pi))
# output = f"pi = {pi}"
# print(output)
# first_number = input("Please enter an Integer: ")
# second_number = input("Please enter another integer: ")
# print (int(first_number) + int(second_number))
# print (float(first_number) + float(second_number))

# Get the current date and time so we need to use the datetime library
# from datetime import datetime, timedelta

# current_datatime = datetime.now()
# print(current_datatime)
# print("Today is " + str(current_datatime))
# one_day = timedelta(days=1)
# yesterday = current_datatime - one_day
# print("yesterday was " + str(yesterday))

# your_birthday = input("Please enter your birthday (dd/mm/yyyy): ")
# birthday_date = datetime.strptime(your_birthday, "%d/%m/%Y")
# print("Your Birthday you entered was " + str(birthday_date))
# one_week = timedelta(weeks=1)
# last_week = current_datatime - one_week
# print ("Last week was " + str(last_week))

# print("Day " + str(current_datatime.day))
# print("Month " + str(current_datatime.month))
# print("Year " + str(current_datatime.year))

# print("Hours " + str(current_datatime.hour))
# print("Minutes " + str(current_datatime.minute))
# print("Seconds " + str(current_datatime.second))

# ERROR HANDLING

# x = 23
# y = 0

# print()
# try:
#     print(x / y)
# except ZeroDivisionError as e:
#     print("Division by zero not allowed")
# else:
#     print("Something else went wrong here")
# finally:
#     print("This is our clean up copy")

# IF STATEMENTS
# price = input("Please enter how much you paid ")
# price = float(price)
# if price >= 1.00:
#     tax = 0.7
#     # print("Your tax rate is " + str(tax))
# else:
#     tax = 0.00
# print("Teh tax rate is " + str(tax))

# COMPARING STRINGS
# country_from = input("Please enter your home country: ")
# if country_from.lower() == "canada":
#     print("Hey, you must like hockey!!")
# else:
#     print("you are not from canada then!")

# MULTIPLE CONDICIONS

# country_from = input("Please enter your home country: ")
# if country_from.capitalize() == "Canada":
#     province = input("Enter the province you are from: ")
#     if province.capitalize() in("Alberta", "Nunavut"):
#         tax = 0.5
#     elif province.capitalize() == "Ontario":
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0.0
# print ("Your tax is: " + str(tax))

# USING 'AND' or 'OR'
# gpa = float(input('Please enter your Grade Poinr Average: '))
# lowest_grade = float(input('Please enter your Lowest Grade: '))
# if gpa >= 0.85 and lowest_grade >= 0.70:
#     print('You made honour roll')
#     honour_roll = True
# else:
#     honour_roll = False

# if honour_roll:
#     print('You made Honour Roll')
# else:
#     print('Your are not Honour Roll')

# LISTS WHICH ARE COLLECTIONS OF ITEMS

# names = ['Luis', 'Sinisterra', 'Bill', 'Carlos']
# names.insert(0, 'Robert')
# print(names)
# presenters = names[1:3]
# print(presenters)
# presenters = names[ :3]
# print(presenters)
# scores = []
# scores.append(20)
# scores.append(80)
# scores.append(99)
# print(scores)
# print(scores[2])   # collections are zero-indexed
# print(len(scores))
# names.sort()
# print(names)


# ARRAYS FOR NUMERICAL ONLY
# from array import array
# scores = array('i')
# scores.append(89)
# scores.append(78)
# print(scores)
# print(scores[0])
# print(len(scores))

# DICTIONARIES
# person = {'first': 'Lucho'}
# person['last'] = 'Munes'
# print(person)
# print(person['last'])

# COMBINE DICTIONARIES AND LISTS
# luis = {}
# luis['first'] = 'Luis'
# luis['last'] = 'Sinistera'

# mariana = {}
# mariana['first'] = 'Mariana'
# mariana['last'] = 'Sinistera'

# people = []
# people.append(luis)
# people.append(mariana)
# print(people)
# print(people[0])
# people.append({'first': 'Bill', 'last': 'Gates'})
# print(people)

# LOOPS
# for name in ['luis', 'mariana']:
#     print(name)

# names = ['Luis', 'Mariana']
# index = 0
# while index < len(names):
#     print('while ' + names[index])
#     index = index + 1

# for people in names:
#     print('for ' + people)

# FUNCTIONS
# from datetime import datetime
# def print_time (task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = 'Luis'
# print_time('First name assined')

# for x in range(0,10):
#     print(x)
# print_time('Loop completed')

# RETURN THE INITIAL OF SOMEONE'S NAME

# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input('Please entere your first name: ')
# first_name_initial = get_initial(first_name)

# middle_name = input ('Please enter your middle name: ')
# middle_name_initial = get_initial(middle_name)

# last_name = input ('Please enter your last name: ')
# last_name_initial = get_initial(last_name)

# print('Your name initials are: ' + first_name_initial + middle_name_initial + last_name_initial)

# PARAMETERIZED FUNCTIONS
# def get_initial(name, force_uppercase = True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input('Please entere your first name: ')
# ways to call the function
# the force_uppercase defaults to False
# first_name_initial = get_initial(first_name)
# first_name_initial = get_initial(first_name, False)
# the following makes the code more readible by using named parameters
# first_name_initial = get_initial(force_uppercase = False, name = first_name)

# print('Your name initials are: ' + first_name_initial)

# MODULES, PUBLISHED COLECTION OF MODULES CALLED PACKAGES ('Python Package Index' on the internet)
# import a module as namespace
# import helpers
# helpers.display('Not a warning!!')

# # import all into current namespace
# from helpers import *
# display('Not a warning!!')

# #import specific item(s) into current namespace
# from helpers import display
# display('Not a warning!!')

# # INSTALLING PACKAGES
# #install an individual package
# pip install colorama

# #install from a list of packages
# pip install -r requirements.txt

# # requirements.txt
# colorama


# # VIRTUAL INVIRONMENTS
# # Creating Virtual Enviroments
# pip install virtualenv

# Windows System
# python -m venv <folder name>
# OSX/Linux (bash)
# virtualenv <folder name>

import requests

import math
import os

import sys
print (sys.version)
r = requests.get("https://coreyms.com")
print(r.status_code)
