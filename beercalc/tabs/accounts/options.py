# -*- coding: utf-8 -*-
import gtk
from .edit_account import AccountDialog
from beercalc.lib.widget import StockButton

class OptionsContainer(gtk.VBox):
    def __init__(self, treeview):
        gtk.VBox.__init__(self)
        
        button_add = AddButton(treeview.store)
        button_delete = DeleteButton(treeview)
        self.add(button_add)
        self.add(button_delete)
        self.child_set_property(button_add, "expand", False)
        self.child_set_property(button_delete, "expand", False)


class AddButton(StockButton):
    def __init__(self, store):
        StockButton.__init__(self, u"_Tilføj", gtk.STOCK_ADD)
        self.store = store

    def OnClick(self, button):
        AccountDialog(self.get_toplevel(), self.store)

class DeleteButton(StockButton):
    def __init__(self, treeview):
        StockButton.__init__(self, u"_Slet", gtk.STOCK_DELETE)
        self.treeview = treeview
    
    def OnClick(self, button):
        self.treeview.remove_selected()
