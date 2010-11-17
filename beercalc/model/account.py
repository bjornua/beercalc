# -*- coding: utf-8 -*-
from beercalc.lib.types import DKK
from beercalc.lib import Observable

class Account(Observable):
    def __init__(self, name = None, email = None, type = None, entries = [], misc = None):
        Observable.__init__(self)
        self._name    = name
        self._email   = email
        self._type    = type
        self._entries = entries
        self._misc    = misc

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
