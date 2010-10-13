# -*- coding: utf-8 -*-
import gtk

from .products import ProductsTab

class MainTabs(gtk.Notebook):
    def __init__(self):
        super(type(self), self).__init__()
        self.products = ProductsTab()
        
        for x in (self.products,):
            self.append_page(x, gtk.Label(x.title))
