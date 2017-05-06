# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:33:04 2017

@author: Dylan
"""

from blotto import best_response_one_day, enumerate_strategies1, levelkResponse
import pdb

def test_best_response_one_day():
    if ([3,1,2] != best_response_one_day([2,3,1])):
        print("Failed [2,3,1] best response.");
    
    if ([0,0,1,0,0] != best_response_one_day([1000,1000,999,1000,1000], 1)):
        print("Failed [big, big, small, big, big] case.")
    print("Passed")
    
    else: 
        print("Passed")
        
            
    
    print("In this case, level 0 switches but level 1 does not:")
    print(levelkResponse([1,8,8,1], [1,2,3,10], 0))
    print(levelkResponse([1,8,8,1], [1,2,3,10], 1))
    
    print("In this case, level 0 switches, level 1 switches to something else:")
    print(levelkResponse([1,8,8,2], [1,2,3,10], 0))
    print(levelkResponse([1,8,8,2], [1,2,3,10], 1))
    
def test_levelkResponse():
    print("In this case, level 0 switches but level 1 does not:")
    print(levelkResponse([1,8,8,1], [1,2,3,10], 0))
    print(levelkResponse([1,8,8,1], [1,2,3,10], 3))
    print(levelkResponse([1,8,8,2], [1,2,3,10], 0))
    print(levelkResponse([1,8,8,2], [1,2,3,10], 3))
    
    return True;

def test_enumerate_strategies():
    print("Testing enumeration of 10 soldiers on four battlefields")
    
    l = enumerate_strategies1(10,4,[],[])
    fail = False
    print [sum(s) for s in l]
    #for (s in l):
    #    if sum(s) != 10:
    #        fail = True;
            
    #if (!fail):
    ##   print('Right number of soldiers')
    if (len(enumerate_strategies1(10,4,[],[])) == (13*12*11)/(3*2)):
        print("Right number")
    

if __name__ == "__main__":
    test_enumerate_strategies()
    test_best_response_one_day();
    print("----------\n")
    test_levelkResponse()
