#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Code goes over here.
    print("Hello world!")
    
    
    first_grade = int( input("Please, enter the first grade: "))
    second_grade = int( input(".. the second grade: " ))
    third_grade = int( input(".. the third grade: "))
    fourth_grade = int( input(".. the fourth grade: "))
    fifth_grade = int( input(".. the fifth grade: ") )
    
    average_grade = (first_grade + second_grade + third_grade + fourth_grade + fifth_grade)/5
    
    print("Your average grade is:", average_grade)
    return 0

if __name__ == "__main__":
    main()
