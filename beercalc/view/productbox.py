# -*- coding: utf-8 -*-
import gtk

from beercalc.lib import Observable, Observers
from .productoptions import OptionsContainer
from .producttable import ProductTable
from .productdialog import ProductDialog


class ProductBox(gtk.VBox, Observable):
    def __init__(self):
        gtk.VBox.__init__(self)
        Observable.__init__(self)
       
        self.title = u"Produkter"
        
        table = ProductTable()
        
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        scrollwin = gtk.ScrolledWindow()
        
        options = OptionsContainer(table)
        
        def add():
            dialog = ProductDialog(self.get_toplevel())
            def submit(name, sell_val, buy_val, misc):
                self.observers.notify("add_product", name, sell_val, buy_val, misc)
            dialog.observers.add("submit", submit)
        options.observers.add("add", add)
        
        def delete():
            table.remove_selection()
        options.observers.add("delete", delete)
        
        for parent, child in (
            (self, hbox),
                (hbox, vbox),
                    (vbox, scrollwin),
                        (scrollwin, table),
                (hbox, options),
        ):
            parent.add(child)
            
        for widget, name, value in (
            (self     , "spacing"          , 0                ),
            (vbox     , "spacing"          , 0                ),
            (hbox     , "spacing"          , 0                ),
            (scrollwin, "vscrollbar-policy", gtk.POLICY_AUTOMATIC),
            (scrollwin, "hscrollbar-policy", gtk.POLICY_NEVER ),
            (scrollwin, "shadow-type"      , gtk.SHADOW_IN    ),
        ):
            widget.set_property(name, value)
            
        hbox.child_set_property(options, "expand", False)
        hbox.child_set_property(vbox   , "expand", True )
        
        self.table = table
        
    def add_product(self, cols, observers):
        observers = Observers()
        observers.
        def removde
        self.table.add_row(cols, observers)

    




