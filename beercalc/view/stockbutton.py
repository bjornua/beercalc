# -*- coding: utf-8 -*-
import gtk
from beercalc.lib import Observable

class StockButton(gtk.Button, Observable):
    def __init__(self, label, stock_image):
        gtk.Button.__init__(self, label)
        Observable.__init__(self)
        self.image = gtk.Image()
        self.image.set_from_stock(stock_image, gtk.ICON_SIZE_MENU)
        self.set_image(self.image)
        self.connect("clicked", self._OnClick)
    
    def _OnClick(self, *args):
        self.observers.notify("clicked")
        

