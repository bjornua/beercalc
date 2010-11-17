# -*- coding: utf-8 -*-
from beercalc.lib import Observable

class Product(Observable):
    def __init__(self, sell_val, buy_val, name = None, count = None, misc = None):
        Observable.__init__(self)
        self._buy_val = buy_val
        self._sell_val = sell_val
        self._name = name
        self._count = count
        self._misc = misc
    
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
    @property
    def misc(self):
        return self._misc
    
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
    @misc.setter
    def misc(self, new):
        old = self._misc
        self._misc = new
        self.observers.notify("changed(misc)", self, old)
    
    def __repr__(self):
        x = list()
        x += ["buy_val = %s" % repr(self.buy_val)]
        x += ["sell_val = %s" % repr(self.sell_val)]
        if(self.name != None):
            x += ["name = %s" % repr(self.name)]
        if(self.count != None):
            x += ["count = %s" % repr(self.count)]
        if(self.misc != None):
            x += ["misc = %s" % repr(self.misc)]
        return "Product(" + ", ".join(x) + ")"
