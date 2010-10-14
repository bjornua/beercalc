# -*- coding: utf-8 -*-
import gtk

from .products import ProductBox

class MainTabs(gtk.Notebook):
    def __init__(self):
        super(type(self), self).__init__()
        
        product = ProductBox()
        self.set_property("show-border", False)
        self.set_property("homogeneous", True)
        
        self.append_page(product, gtk.Label(u"Produkter"))

