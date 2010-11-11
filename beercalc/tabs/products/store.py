# -*- coding: utf-8 -*-
import gtk
import gobject
from beercalc.lib.objects import DKK
from beercalc.lib.misc import Observers


class ProductStore(gtk.ListStore):
    def __init__(self):
        super(type(self), self).__init__(
            gobject.TYPE_PYOBJECT,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
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

    
    def append(self, product):
        iter = gtk.ListStore.append(self)
        row = self[iter]
        row[0] = product
        
        for signal, callback in (
            ("changed(name)"    , update_name    ),
            ("changed(count)"   , update_count   ),
            ("changed(sell_val)", update_sell_val),
            ("changed(buy_val)" , update_buy_val )
        ):
            product.observers.add(signal, callback, row)
            callback(row, product)
        
        return iter

def update_name(row, product, *args):
    row[1] = product.name
def update_count(row, product, *args):
    if product.count is None:
        row[2] = ""
    else:
        row[2] = product.count
def update_sell_val(row, product, *args):
    row[3] = product.sell_val
def update_buy_val(row, product, *args):
    row[4] = product.buy_val
