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
    return True;


if __name__ == "__main__":
    test_best_response_one_day();