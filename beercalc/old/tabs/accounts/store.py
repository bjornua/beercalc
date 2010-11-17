# -*- coding: utf-8 -*-
import gtk
import gobject
from beercalc.lib.objects import DKK
from beercalc.lib import Observers

class AccountStore(gtk.ListStore):
    def __init__(self):
        super(type(self), self).__init__(
            gobject.TYPE_PYOBJECT,
            gobject.TYPE_STRING, # Type
            gobject.TYPE_STRING, # Name
            gobject.TYPE_STRING, # Email
            gobject.TYPE_STRING, # Balance
        )
        self._total = DKK(0)
        self.observers = Observers()
    
    @property
    def total(self):
        return self.total
    
    @total.setter
    def total(self, new):
        old = self._buy_val
        self._buy_val = new
        self.observers.notify("changed(total)", self, old)
    
    def append(self, account):
        iter = gtk.ListStore.append(self)
        row = self[iter]
        row[0] = account
        
        for signal, callback in (
            ("changed(type)"   , update_type   ),
            ("changed(name)"   , update_name   ),
            ("changed(email)"  , update_email  ),
            ("changed(balance)", update_balance),
        ):
            account.observers.add(signal, callback, row)
            callback(row, account)
        
        return iter

def update_type(row, account, *args):
    row[1] = account.type
def update_name(row, account, *args):
    row[2] = account.name
def update_email(row, account, *args):
    row[3] = account.email
def update_balance(row, account, *args):
    row[4] = account.get_balance()

