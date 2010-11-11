# -*- coding: utf-8 -*-
class DKK(object):
    def __init__(self, integer = 0):
        self.integer = integer
    
    def __add__(self, other):
        return DKK(self.integer + other.integer)
    
    def __str__(self):
        integer = str(self.integer // 100)
        fraction = str(self.integer % 100)
        
        # Add thousands seperator
        integer = integer[::-1]
        integer = ".".join(integer[i:i+3] for i in range(0, len(integer), 3))
        integer = integer[::-1]
        
        # Zero pad 
        fraction = ("0" + fraction)[-2:]
        
        return integer + "," + fraction + " kr."
    
    def __repr__(self):
        if self.integer == 0:
            return "DKK()"
        return "DKK(integer = %s)" % repr(self.integer)
