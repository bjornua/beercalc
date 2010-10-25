# -*- coding: utf-8 -*-
import gtk
import gobject
import uuid

class AccountStore(gtk.ListStore):
    def __init__(self):
        super(type(self), self).__init__(
            gobject.TYPE_PYOBJECT, # Account object
            gobject.TYPE_STRING,   # Name
        )
        self.total = 0
        
    def append_new(self):
        iter = self.append((uuid.uuid4().get_hex(), ""))
        self.set(iter, name = "Ny konto")
        return iter
        
    def set(self, iter, name = None):
        if(text != None):    
            super(type(self), self).set(iter, 1, text)

