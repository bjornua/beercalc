# -*- coding: utf-8 -*-
import gtk

from .products import ProductBox
from .accounts import AccountBox

class MainTabs(gtk.Notebook):
    def __init__(self):
        super(type(self), self).__init__()
        
        product = ProductBox()
        account = AccountBox()

        self.set_property("show-border", False)
        self.set_property("homogeneous", True )
        
        self.append_page(product, gtk.Label(u"Produkter"))
        self.append_page(account, gtk.Label(u"Konti"))

