# -*- coding: utf-8 -*-
import gtk
from .options import OptionsContainer
from .store import ProductStore
from .table import ProductStatus, ProductTable
class ProductsTab(gtk.HBox):
    def __init__(self):
        super(type(self), self).__init__()
        self.title = u"Produkter"
        
        store = ProductStore()
        status = ProductStatus()
        table = ProductTable(store, status)
        
        vbox = gtk.VBox()
        
        scrollwin = gtk.ScrolledWindow()
        
        options = OptionsContainer(table)
        
        vbox.add(scrollwin)
        scrollwin.add(table)
        vbox.add(status)
        self.add(vbox)
        self.add(options)
        
        scrollwin.set_property("vscrollbar-policy", gtk.POLICY_ALWAYS)
        scrollwin.set_property("hscrollbar-policy", gtk.POLICY_NEVER)
        vbox.child_set_property(status, "expand", False)
        self.child_set_property(vbox, "expand", True)
        self.child_set_property(options, "expand", False)
  
