# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:18:54 2023

@author: smith
"""

#PassingUnderSpeedometerv0.9


    
while True: #starts loop

    #variables
    time = float(input('Lap time in seconds: '))

    trklen = float(input('Track length in miles: '))

    mph = float((trklen/time)*3600)

    print(mph)
        

    user_input = input("Continue? y/n: ")
    
    if user_input.lower() == 'n':
        print("Exiting")
        

 
    
