# -*- coding: utf-8 -*-
import gtk
from .stockbutton import StockButton
from beercalc.lib import Observable

class OptionsContainer(gtk.VBox, Observable):
    def __init__(self, treeview):
        gtk.VBox.__init__(self)
        Observable.__init__(self)

        for label, stock, action in (
            ("_Tilføj" , gtk.STOCK_ADD   , self._OnAdd),
            ("_Redigér", gtk.STOCK_EDIT  , self._OnEdit),
            ("_Slet"   , gtk.STOCK_DELETE, self._OnDelete),
        ):
            button = StockButton(label, stock)
            button.observers.add("clicked", action)
            self.add(button)
            self.child_set_property(button, "expand", False)

    def _OnAdd(self):
        self.observers.notify("add")
    def _OnEdit(self):
        self.observers.notify("edit")
    def _OnDelete(self):
        self.observers.notify("delete")
