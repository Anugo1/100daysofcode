# print("hello " + input('what be your name? + "!'))

# input() will get user input in console and
# then print  the hello + user input
# The len() function calculates the length of an input=input()
# and prints it out using the print function.
# from os import name

# Name_e = input("Name: ")
# print(type(Name_e))
# print(len(Name))

# another way of writing it :
# print(len(input("name: ")))

# converting to string.
# num_char = len(input("What is your name? "))
#
# new_num_char = str(num_char)
#
# print("Your name has " + new_num_char + " characters.")

# a = str(123)
# print(a)
# check the data type of two_digit_number
# two_digit_number = input("Type a two digit number ")
#
# # get the first and second digits using subscripting then convert str to int
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# # add the two digits together
# result = int(first_digit) + int(second_digit)
# print(result)

# height = input("enter your height: ")
# weight = input("enter your weight:  ")
#
# # print(type(height))
# Bmi = int(weight) / float(height) ** 2
#
# new_bmi = int(Bmi)
#
# ano_bmi = str(new_bmi)
# # printing as  a string:
#
# print("bmi is " + ano_bmi + "")
#
# # printing it as just an integer:
#
# bmiInt = int(Bmi)
# print(bmiInt)

# print(type(round(9//2, 2)))
# score = 37.5
# score += 3
# print(score)
# # # f-string
# # print(f"your score is {score}")
#
# age = input("What is your current age: ")
# new_age = int(age)
#
# age_left = 90 - new_age
# days_remaining = 365 * age_left
# weeks_remaining = 52 * age_left
# months_remaining = 12 * age_left
#
# print(f"your have {days_remaining} days , {weeks_remaining} weeks and {months_remaining} months left.")
# print("Welcome to the tip calculator.")
# total_bill = float(input('What was the total bill? $'))
# percentage_tip = int(input("What percentage tip would you like to give? 12,15,20 %"))
# num_to_split_bill = int(input("How many people to split bill? "))
#
# billntip = percentage_tip/100 * total_bill + total_bill
# each_bill = round(billntip / num_to_split_bill, 2)
# print(f"Each person should pay ${each_bill}")
# print("Welcome to the tunnel of horror")
# age = int(input("what is your age?: "))
#
# if age >= 18:
#     print("you can enter the tunnel of horrors.")
#     if age == 18:
#         print("You pay #300")
#     elif age <= 21:
#         print("you pay #500")
#     elif age >= 70:
#         print("beware of hrt attacks you pay #200")
#     else:
#         print("you pay #700")
# else:
#     print("you are too young to enter the tunnel of horrors.")

# code practice:
# number = int(input("Which number do you want to check? "))
# check_num = number % 3
# if check_num == 0:
#     print("This is divided by 3")
# else:
#     print("This is not divided by 3.")

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = weight / height ** 2
# new_bmi = (round(bmi, 1))
# if new_bmi <= 18.5:
#     print(f"your bmi is{new_bmi} , you are underweight.")
# elif new_bmi <= 25:
#     print(f"your bmi is {new_bmi}, you have a normal weight.")
# elif new_bmi <= 30:
#     print(f"your bmi is {new_bmi}, you are overweight.")
# elif new_bmi <= 35:
#     print(f"your bmi is {new_bmi}, you are obese.")
# else:
#     print(f"your bmi is {new_bmi},you are clinically obese.")