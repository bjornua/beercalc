# -*- coding: utf-8 -*-
import gtk

class OptionsContainer(gtk.VBox):
    def __init__(self, treeview):
        super(type(self), self).__init__()
        self.treeview = treeview
        self.button_add = AddButton(treeview)
        self.button_delete = DeleteButton(treeview)
        self.add(self.button_add)
        self.add(self.button_delete)
        self.child_set_property(self.button_add, "expand", False)
        self.child_set_property(self.button_delete, "expand", False)

class AddButton(gtk.Button):
    def __init__(self, treeview):
        super(type(self), self).__init__(u"_Tilføj")
        self.treeview = treeview
        self.image = gtk.Image()
        self.image.set_from_stock(gtk.STOCK_ADD, gtk.ICON_SIZE_MENU)
        self.set_image(self.image)
        self.store = treeview.store
        self.col_desc = self.treeview.col_desc
        self.connect("clicked", self.OnClick)

    def OnClick(self, button):
        iter = self.store.append_new()
        path = self.treeview.store.get_path(iter)
        self.treeview.set_cursor(path, self.col_desc, start_editing = True)

class DeleteButton(gtk.Button):
    def __init__(self, treeview):
        super(type(self), self).__init__(u"_Slet")
        self.image = gtk.Image()
        self.image.set_from_stock(gtk.STOCK_DELETE, gtk.ICON_SIZE_MENU)
        self.set_image(self.image)
        self.treeview = treeview
        self.connect("clicked", self.OnClick)
    
    def OnClick(self, button):
        store, paths = self.treeview.get_selection().get_selected_rows()
        references = [gtk.TreeRowReference(store, path) for path in paths]
        
        for reference in references:
            path = reference.get_path()
            iter = store.get_iter(path)
            store.remove(iter)
