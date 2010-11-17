# -*- coding: utf-8 -*-
import gtk
from beercalc.lib import Observable

from .maintabs import MainTabs
from .menubar import MenuBar

class MainWindow(gtk.Window, Observable):
    def __init__(self):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        Observable.__init__(self)
        vbox = gtk.VBox()
        menu = MenuBar()
        tabs = MainTabs()

        self.acg = gtk.AccelGroup()
        self.add_accel_group(self.acg)
        
        self.add(vbox)
        vbox.add(menu)
        vbox.add(tabs)
        
        self.get_settings().set_long_property("gtk-button-images", True, "")
        self.set_property("default-height", 400              )
        self.set_property("default-width" , 400              )
        self.set_property("title"         , u"RKG Ølregnskab")
        vbox.child_set_property(menu, "expand", False)

        self.connect("destroy", self._on_destroy)
        
        tabs.observers.add("add_product", self._on_add_product)
        
        self.show_all()
        
        self.tabs = tabs

    def _on_destroy(self, *args):
        self.observers.notify("quit")
    
    def _on_add_product(self, name, sell_val, buy_val, misc):
        self.observers.notify("add_product", name, sell_val, buy_val, misc)
    
    def add_product(self, cols, observers):
        self.tabs.add_product(cols, observers)
