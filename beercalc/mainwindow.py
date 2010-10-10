# -*- coding: utf-8 -*-
import gtk
from .maintabs import MainTabs


class MainWindow(gtk.Window):
    def __init__(self):
        super(type(self), self).__init__(gtk.WINDOW_TOPLEVEL)
        self.set_title(u"BeerCalc")
        self.connect("destroy", self.OnDestroy)
        self.maintabs = MainTabs()
        self.add(self.maintabs)
        self.set_default_size(400,400)
        self.show_all()

    def OnDestroy(self, window):
        gtk.main_quit()
