# -*- coding: utf-8 -*-
import gtk

class OptionsContainer(gtk.VBox):
    def __init__(self, treeview):
        super(type(self), self).__init__()
        self.treeview = treeview
        self.store = treeview.store
        self.button_add = AddButton(treeview)
        self.button_delete = DeleteButton(treeview)
        self.button_edit = EditButton(treeview)
        self.add(self.button_add)
        self.add(self.button_delete)
        self.add(self.button_edit)
        self.child_set_property(self.button_add, "expand", False)
        self.child_set_property(self.button_delete, "expand", False)
        self.child_set_property(self.button_edit, "expand", False)

class AddButton(gtk.Button):
    def __init__(self, treeview):
        super(type(self), self).__init__(u"_Tilføj")
        self.treeview = treeview
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
        self.treeview = treeview
        self.connect("clicked", self.OnClick)
    
    def OnClick(self, button):
        store, iter = self.treeview.get_selection().get_selected()
        
        if iter != None:
            store.remove(iter)
        
class EditButton(gtk.Button):
    def __init__(self, treeview):
        super(type(self), self).__init__(u"_Redigér")
        self.treeview = treeview

