#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Code goes over here.
    print("Hello world!")
    print("My name is Charlotte")
    # age is a variable 
    age = int( input("How old are you?"))
    # forcing python to know that this is an integer
    print("Your age is:", age)

    print("Please enter your best 5 grades this year")
    grade_one = int( input("Please, enter the first grade"))
    grade_two = int( input("... the second grade"))
    grade_three = int( input("... the third grade"))
    grade_four = int( input("... the fourth grade"))
    grade_five = int( input("... the fifth grade"))
    
    average_grade = (grade_one + grade_two + grade_three + grade_four + grade_five)/5
    
    print("Your average grade is:", average_grade)
    
    return 0
    
if __name__ == "__main__":
    main()
