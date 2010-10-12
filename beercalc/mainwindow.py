# -*- coding: utf-8 -*-
import gtk
from .maintabs import MainTabs
from .menubar import MenuBar

class MainWindow(gtk.Window):
    def __init__(self):
        super(type(self), self).__init__(gtk.WINDOW_TOPLEVEL)
        self.get_settings().set_long_property("gtk-button-images", True, "burp")
        self.acg = gtk.AccelGroup()
        self.add_accel_group(self.acg)
        self.set_title(u"BeerCalc")
        self.connect("destroy", self.OnDestroy)
        self.mainTabs = MainTabs()
        self.menuBar = MenuBar()
        self.vbox = gtk.VBox()
        self.vbox.add(self.menuBar)
        self.vbox.child_set_property(self.menuBar, "expand", False)
        self.vbox.add(self.mainTabs)
        self.add(self.vbox)
        self.set_default_size(400,400)
        self.show_all()

    def OnDestroy(self, window):
        gtk.main_quit()
