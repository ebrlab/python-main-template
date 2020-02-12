#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Code goes over here.
    print("Hello world!")

    print("Please enter your best 5 grades this year")
    grade_one = int( input("Please, enter the first grade"))
    grade_two = int( input("... the second grade"))
    grade_three = int( input("... the third grade"))
    grade_four = int( input("... the fourth grade"))
    grade_five = int( input("... the fifth grade"))
    
    average_grade = (grade_one + grade_two + grade_three + grade_four + grade_five)/5
    
    print("Your average grade is:", average_grade)
    
    print("Thank you!")
    
    
    return 0
    
if __name__ == "__main__":
    main()
