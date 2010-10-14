# -*- coding: utf-8 -*-
import gtk
from .tabs import MainTabs
from .menubar import MenuBar

class MainWindow(gtk.Window):
    def __init__(self):
        super(type(self), self).__init__(gtk.WINDOW_TOPLEVEL)
        vbox = gtk.VBox()
        menu = MenuBar()
        tabs = MainTabs()

        self.acg = gtk.AccelGroup()
        self.add_accel_group(self.acg)
        
        self.add(vbox)
        vbox.add(menu)
        vbox.add(tabs)
        
        self.get_settings().set_long_property("gtk-button-images", True, "")
        self.set_property("default-height", 400        )
        self.set_property("default-width" , 400        )
        self.set_property("title"         , u"BeerCalc")
        vbox.child_set_property(menu, "expand", False)

        self.connect("destroy", self.OnDestroy)
        
        self.show_all()

    def OnDestroy(self, window):
        gtk.main_quit()
