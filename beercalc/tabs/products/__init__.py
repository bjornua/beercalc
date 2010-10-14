# -*- coding: utf-8 -*-
import gtk
from .options import OptionsContainer
from .store import ProductStore
from .table import ProductStatus, ProductTable
class ProductBox(gtk.VBox):
    def __init__(self):
        super(type(self), self).__init__()
        self.title = u"Produkter"
        
        store = ProductStore()
        status = ProductStatus()
        table = ProductTable(store, status)
        
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        scrollwin = gtk.ScrolledWindow()
        
        options = OptionsContainer(table)
        
        for parent, child in (
            (self, hbox),
                (hbox, vbox),
                    (vbox, scrollwin),
                        (scrollwin, table),
                    (vbox, status),
                (hbox, options),
        ):
            parent.add(child)
            
        for widget, name, value in (
            (self     , "spacing"          , 0                ),
            (vbox     , "spacing"          , 0                ),
            (hbox     , "spacing"          , 0                ),
            (scrollwin, "vscrollbar-policy", gtk.POLICY_ALWAYS),
            (scrollwin, "hscrollbar-policy", gtk.POLICY_NEVER ),
            (scrollwin, "shadow-type"      , gtk.SHADOW_IN    ),
        ):
            widget.set_property(name, value)
            
        vbox.child_set_property(status , "expand", False)
        hbox.child_set_property(options, "expand", False)
        hbox.child_set_property(vbox   , "expand", True )
        

