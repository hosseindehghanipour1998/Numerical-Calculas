# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:03:53 2020

@author: Hossein
"""
import cmath as mathematician
import random

def bairstow( roots_list , coefficients_list , r0 , s0 ):
    # coefficients_list = ax^2 + bx + c -> [c,a,b]
    tolerance = 10**-6
    n = len(coefficients_list) - 1

    
    #if there was only one Number in the input
    if(n == 0):
        return None
    
    # Polynomial Degree 1
    elif ( n == 1 ):
        return float(coefficients_list[1]/coefficients_list[0])*-1
    
    #polynomial Degree 2
    elif ( n == 2 ):
        #b^2 - 4ac
        delta = coefficients_list[1]**2 - 4*coefficients_list[2]*coefficients_list[0]
        root1 = (-coefficients_list[1] + mathematician.sqrt(delta))/(2.0*coefficients_list[2])
        print("Root1 : " , root1)
        root2 = (-1*coefficients_list[1] - mathematician.sqrt(delta))/(2.0*coefficients_list[2])
        print("Root2 : " , root1)
        roots_list.append(root1)
        roots_list.append(root2)
        
    #if the polynomial had a degree > 2
     else:
         
         b = [0] * ( n + 1 )
         #Calculate B's
         b[n] = coefficients_list[n]
         b[n-1] = coefficients_list[n-1] + r0 * b[n]
         for i in range(n-2 , -1 , -1):
             b[i] = coefficients_list[i] + r0 * b[i+1] + s0 * b[i+2]
        #Calculate C's
        c = [0] * ( n + 1 )
        c[n] = b[n]
        c[n-1] = b[n-1] + r0 * c[n] 
        for i in range(n-2 , -1 , -1):
            c[i] = b[i] + r0 * c[i+1] + s0 * c[i+2]
        
    
################### MATRIX OPERATIONS #################33

def calculateDeterminant(index00 , index01 , index10 , index11 ):
    return ( index00 * index11 - index01*index10 ) 


def atoi(a_list):
    return list(map(lambda x : int(x) , a_list))
    




############## MAIN #####################
def main():
    #INPUT 
    #n = input("Enter Polynomial's Degree : ")
    #inputCoefficients = list(reversed(input().split(' ')))
    inputCoefficients = [-6 , 1 , 1]
    #inputCoefficients = atoi(inputCoefficients)
    
    #NEEDED ELEMENTS
    roots_list = [] 
    s0 = 0.1
    r0 = 0.1
    bairstow(roots_list , inputCoefficients , r0 , s0)
    print("Input Coefficints : " , inputCoefficients)
    print("Roots : " , roots_list)

    
main() 


