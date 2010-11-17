# -*- coding: utf-8 -*-
from beercalc.lib import Observable

class AccountEntry(Observable):
    def __init__(self, amount, date = None):
        Observable.__init__(self)
        self.amount = amount
        self.date = date
    
    def __repr__(self):
        x = ["amount = %s" % repr(self.amount)]
        if(self.date != None):
            x += ["date = %s" % repr(self.date)]
        return "AccountEntry(" + ", ".join(x) + ")"
