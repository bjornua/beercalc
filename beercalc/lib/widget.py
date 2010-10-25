# -*- coding: utf-8 -*-
import gtk

class StockButton(gtk.Button):
    def __init__(self, label, stock_image):
        gtk.Button.__init__(self, label)
        self.image = gtk.Image()
        self.image.set_from_stock(stock_image, gtk.ICON_SIZE_MENU)
        self.set_image(self.image)
        self.connect("clicked", self.OnClick)

