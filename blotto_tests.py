# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:33:04 2017

@author: Dylan
"""

from blotto import best_response_one_day

def test_best_response_one_day():
    if ([3,1,2] != best_response_one_day([2,3,1])):
        print("Failed [2,3,1] best response.");
    
    if ([0,0,1,0,0] != best_response_one_day([1000,1000,999,1000,1000], 1)):
        print("Failed [big, big, small, big, big] case.")
    else 
        print("Passed")
        
            
    
    print("In this case, level 0 switches but level 1 does not:")
    print(levelkResponse([1,8,8,1], [1,2,3,10], 0))
    print(levelkResponse([1,8,8,1], [1,2,3,10], 1))
    
    print("In this case, level 0 switches, level 1 switches to something else:")
    print(levelkResponse([1,8,8,2], [1,2,3,10], 0))
    print(levelkResponse([1,8,8,2], [1,2,3,10], 1))
    
    
        
    return True;


if __name__ == "__main__":
    test_best_response_one_day();
