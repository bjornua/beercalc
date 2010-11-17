# -*- coding: utf-8 -*-
import gtk
from beercalc.lib import Observable
from .productbox import ProductBox

class MainTabs(gtk.Notebook, Observable):
    def __init__(self):
        gtk.Notebook.__init__(self)
        Observable.__init__(self)

        productbox = ProductBox()
        
        def add_product(name, sell_val, buy_val, misc):
            self.observers.notify("add_product", name, sell_val, buy_val, misc)
        productbox.observers.add("add_product", add_product)

        self.set_property("show-border", False)
        self.set_property("homogeneous", True )
        
        self.append_page(productbox, gtk.Label(u"Produkter"))
        
        self.productbox = productbox
        

    def add_product(self, cols, observers):
        self.productbox.add_product(cols, observers)
