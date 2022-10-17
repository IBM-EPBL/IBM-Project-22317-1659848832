# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import time
while(1):
    temp=random.uniform(10.0,40.0)
    humid=random.randint(30,90)
    print("\nTemperature : {:.2f}*C Humidity : {}%" .format(temp,humid))
    if temp>30:
        print("\n Warning: Temperature is high")
    else:
        print("\n Normal Temperature")
    time.sleep(1)

