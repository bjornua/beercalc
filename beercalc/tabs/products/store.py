# -*- coding: utf-8 -*-
import gtk
import gobject
import uuid

class ProductStore(gtk.ListStore):
    def __init__(self):
        super(type(self), self).__init__(
            gobject.TYPE_PYOBJECT,
            gobject.TYPE_PYOBJECT,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
        )
        self.total = 0
        
    def append_new(self):
        iter = self.append((uuid.uuid4().get_hex(), 0, "", ""))
        self.set(iter, text = "Ny udgift", amount = 0)
        return iter
    
    def remove(self, iter):
        self.total -= self.get_value(iter, 1)
        super(type(self), self).remove(iter)
        
    
    def set(self, iter, text = None, amount = None):
        if(amount != None):
            self.total += amount - self.get_value(iter, 1)
            integer  = str(amount // 100)
            integer = integer[::-1]
            integer = ".".join(integer[i:i+3] for i in range(0, len(integer), 3))
            integer = integer[::-1]
            fraction = str(amount % 100)
            fraction = (fraction + "0")[:2]
            amount_text = integer + "," + fraction + " kr."

            super(type(self), self).set(iter, 1, amount, 3, amount_text)
        if(text != None):    
            super(type(self), self).set(iter, 2, text)

