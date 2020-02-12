#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Code goes over here.
    print("Hello world!")
<<<<<<< HEAD
    print("My name is Charlotte")
    # age is a variable 
    age = int( input("How old are you?"))
    # forcing python to know that this is an integer
    print("Your age is:", age)
=======
    
    
    first_grade = int( input("Please, enter the first grade: "))
    second_grade = int( input(".. the second grade: " ))
    third_grade = int( input(".. the third grade: "))
    fourth_grade = int( input(".. the fourth grade: "))
    fifth_grade = int( input(".. the fifth grade: ") )
    
    average_grade = (first_grade + second_grade + third_grade + fourth_grade + fifth_grade)/5
    
    print("Your average grade is:", average_grade)
    return 0
>>>>>>> 0e8a7cbdda3699c5d01f0632d8a2108b758639f8

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
