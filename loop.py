#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 22:02:39 2018

@author: akshay
"""

n=int(input("enter a number > 0 : "))

if (n <= 0) :
    print("error")

while (n >= 0) :
    print("n: " + str(n))
    n-=1
    
n=int(input("enter a number > 0 : "))
if (n <= 0) :
    print("error")

while n in range(n%2,n,3) :
    print("test")


end=17
i=1
j=1
while j <= end :
    j+=1 
    i+=j
print(i)