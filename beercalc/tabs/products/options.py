# -*- coding: utf-8 -*-
import gtk
from .add_product import ProductDialog

class OptionsContainer(gtk.VBox):
    def __init__(self, treeview):
        super(type(self), self).__init__()
        
        button_add = AddButton(treeview)
        button_delete = DeleteButton(treeview)
        self.add(button_add)
        self.add(button_delete)
        self.child_set_property(button_add, "expand", False)
        self.child_set_property(button_delete, "expand", False)

class OptionButton(gtk.Button):
    def __init__(self, label, stock_image):
        gtk.Button.__init__(self, label)
        self.image = gtk.Image()
        self.image.set_from_stock(stock_image, gtk.ICON_SIZE_MENU)
        self.set_image(self.image)
        self.connect("clicked", self.OnClick)

class AddButton(OptionButton):
    def __init__(self, treeview):
        OptionButton.__init__(self, u"_Tilføj", gtk.STOCK_ADD)
        self.treeview = treeview

    def OnClick(self, button):
        ProductDialog(self.get_toplevel(), self.treeview.store)
        self.treeview.store

class DeleteButton(OptionButton):
    def __init__(self, treeview):
        OptionButton.__init__(self, u"_Slet", gtk.STOCK_DELETE)
        self.treeview = treeview
    
    def OnClick(self, button):
        self.treeview.remove_selected()
