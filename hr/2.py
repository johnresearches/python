import math
import os

import random
import re
import sys
if __name__ == '__main__':
    
    n = int(raw_input().strip())

    
    if n % 2 == 0:
        if n >= 2 and n <= 5:
            print "Not Weird"
        elif n >=6 and n <= 20:
            print "Weird"
        elif n > 20 and n <= 100:
            if n % 2 == 0:
                print "Not Weird"
            else:
                print "Weird"
    else:
        print "Weird" 
