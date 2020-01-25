# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:03:53 2020

@author: Hossein
"""
import cmath as mathematician
import random
import numpy 

def bairstow( roots_list , coefficients_list , r0 , s0 ):

    # coefficients_list = ax^2 + bx + c -> [c,a,b]
    tolerance = 1E-6
    n = len(coefficients_list) - 1

    #if there was only one Number in the input
    if(n == 0):
        return coefficients_list[0]
    
    # Polynomial Degree 1
    elif ( n == 1 ):
        roots_list.append( float(coefficients_list[0]/coefficients_list[1])*-1)
    
    #polynomial Degree 2
    elif ( n == 2 ):
        #b^2 - 4ac
        delta = coefficients_list[1]**2 - 4*coefficients_list[2]*coefficients_list[0]
        root1 = (-coefficients_list[1] + mathematician.sqrt(delta))/(2.0*coefficients_list[2])
        root2 = (-1*coefficients_list[1] - mathematician.sqrt(delta))/(2.0*coefficients_list[2])
        roots_list.append(root1)
        roots_list.append(root2)
        
    #if the polynomial had a degree > 2
    elif (n >= 3 ):
        
        while(True):
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
           
            #Calculating D's
            D  = calculateDeterminant (c[1] , c[2] , c[2] , c[3])
            D1 = calculateDeterminant (-b[0] , c[2] , -b[1] , c[3])
            D2 = calculateDeterminant (c[1] , -b[0] , c[2] , -b[1])
            
            if (  D == 0 ):
                return None
            
            #Delta
            delta_r = float(D1/D)
            r0 = r0 + delta_r
            delta_s = float(D2/D)
            s0 = s0 + delta_s
            
            #check if the difference is greater than our tolerance (epsilon) or not
            if ( abs(b[0]) < tolerance and abs(b[1]) < tolerance ):
                break
        
        #End of While
        dis = (r0)**(2.0) + (4.0 * (s0))
        x1 = (r0 - (mathematician.sqrt(dis)))/(2)
        x2 = (r0 + (mathematician.sqrt(dis)))/(2)
        roots_list.append(x1)
        roots_list.append(x2)
        return bairstow(roots_list , b[2:] , r0 , s0 )
    
###################  Utility Functions #################33

def calculateDeterminant(index00 , index01 , index10 , index11 ):
    return ( index00 * index11 - index01*index10 ) 


def atoi(a_list):
    return list(map(lambda x : int(x) , a_list))
    
def printList(a_message, a_list):
    print(a_message)
    list(map(lambda x : print(x) , a_list))

def sigma(a_list):
    summation = 0 
    for number in a_list :
        if( (number.imag > 0)  or (numpy.iscomplex(number) == False) ):
            summation += number
    return summation

def printOutput(a_complexNumber):
    realPart = a_complexNumber.real
    imaginaryPart = a_complexNumber.imag
    print('%.6f '%realPart ," ", '%.6f'%imaginaryPart )
############## MAIN #####################
    '''
    -3x^5 + 2x^4 + x^3 + 0x^2 - x - 1
    #Sample Input : inputCoefficients = [-3 , 2 , 1 , 0 , -1 , -1]
    '''
def main():
    #Get Input : 
    n = input()
    #print("Sample -> Ax^2 + Bx + C => A B C" )
    #print("Enter The Coefficients as said Above: ")
    inputCoefficients = list(reversed(input().split(' ')))
    inputCoefficients = atoi(inputCoefficients)
    
    #Initial Elemnets and Values
    roots_list = [] 
    #s0 = random.random()
    #r0 = random.random()
    s0 = -1.9
    r0 = -2.1
    #Printing Coefficients
    #print("Input Coefficints : " , inputCoefficients)
    #print("===========================")
    
   #Main Function Call
    bairstow(roots_list , inputCoefficients , r0 , s0)
    
    #Printing Calculated Roots
    #printList("Roots : " , roots_list)
    #print("===========================")
    
    #Printing the output Summation
    #print("Output : ( Positive Roots Summation) ")
    summation = sigma(roots_list)
    printOutput(summation)
########################################## RUN #############   
    
main() 


