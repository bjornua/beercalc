# -*- coding: utf-8 -*-
from .types import DKK
from beercalc.lib.misc import Observers

class Product(object):
    def __init__(self, buy_val, sell_val, name = None, count = None):
        self._buy_val = buy_val
        self._sell_val = sell_val
        self._name = name
        self._count = count
        self.observers = Observers()
    
    @property
    def buy_val(self):
        return self._buy_val
    @property
    def sell_val(self):
        return self._sell_val
    @property
    def name(self):
        return self._name
    @property
    def count(self):
        return self._count
    
    @buy_val.setter
    def buy_val(self, new):
        old = self._buy_val
        self._buy_val = new
        self.observers.notify("changed(buy_val)", self, old)
    @sell_val.setter
    def sell_val(self, new):
        old = self._sell_val
        self._sell_val = new
        self.observers.notify("changed(sell_val)", self, old)
    @name.setter
    def name(self, new):
        old = self._name
        self._name = new
        self.observers.notify("changed(name)", self, old)
    @count.setter
    def count(self, new):
        old = self._count
        self._count = new
        self.observers.notify("changed(count)", self, old)
    
    def __repr__():
        x = list()
        x += ["buy_val = %s" % repr(self.buy_val)]
        x += ["sell_val = %s" % repr(self.sell_val)]
        if(self.name != None):
            x += ["name = %s" % repr(self.name)]
        if(self.count != None):
            x += ["count = %s" % repr(self.count)]
        return "Product(" + ", ".join(x) + ")"

class Account(object):
    def __init__(self, name = None, email = None, type = None, entries = [], misc = None):
        self._name    = name
        self._email   = email
        self._type    = type
        self._entries = entries
        self._misc    = misc
        self.observers = Observers()

    @property
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email
    @property
    def type(self):
        return self._type
    @property
    def misc(self):
        return self._misc
    @property
    def entries(self):
        return self._entries

    @name.setter
    def name(self, new):
        old = self._name
        self._name = new
        self.observers.notify("changed(name)", self, old)
    @email.setter
    def email(self, new):
        old = self._email
        self._email = new
        self.observers.notify("changed(email)", self, old)
    @type.setter
    def type(self, new):
        old = self._type
        self._type = new
        self.observers.notify("changed(type)", self, old)
    @misc.setter
    def misc(self, new):
        old = self._misc
        self._misc = new
        self.observers.notify("changed(misc)", self, old)

    def get_balance(self):
        if len(self.entries) == 0:
            return DKK()
        return reduce(DKK.__add__, (x.amount for x in self.entries))
    
    def __repr__(self):
        x = list()
        if(self._name != None):
            x += ["name = %s" % repr(self._name)]
        if(self._email != None):
            x += ["email = %s" % repr(self._email)]
        if(self._type != None):
            x += ["type = %s" % repr(self._type)]
        if(self._entries != []):
            x += ["entries = %s" % repr(self._entries)]
        if(self._misc != None):
            x += ["misc = %s" % repr(self._misc)]
        return "Account(" + ", ".join(x) + ")"

class AccountEntry(object):
    def __init__(self, amount, date = None):
        self.amount = amount
        self.date = date
    
    def __repr__(self):
        x = ["amount = %s" % repr(self.amount)]
        if(self.date != None):
            x += ["date = %s" % repr(self.date)]
        return "AccountEntry(" + ", ".join(x) + ")"
