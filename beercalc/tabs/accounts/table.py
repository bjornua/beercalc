# -*- coding: utf-8 -*-
import gtk

class AccountTable(gtk.TreeView):
    def __init__(self, store):
        super(type(self), self).__init__(model=store)
        
        self.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        self.store = store

        self.set_property("rules-hint"   , True)
        
        self.set_property("enable-search", False)
        
        self.col_desc = gtk.TreeViewColumn()

        self.cell_desc = gtk.CellRendererText()

        self.col_desc.pack_start(self.cell_desc)
        
        self.col_desc.set_property("title", u"Beskrivelse")
        self.col_desc.set_property("expand", True)
        self.col_desc.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)

        self.cell_desc.set_property("xalign", 0)
        self.cell_desc.set_property("editable", True)
        self.cell_desc.connect("edited", self.OnEditDoneDesc)
        
        self.col_desc.add_attribute(self.cell_desc, 'text', 2)
        
        self.append_column(self.col_desc)

        self.connect("focus-in-event", self.OnFocusIn)
        self.connect("focus-out-event", self.OnFocusOut)
        
    def OnEditDoneDesc(self, cell, path, new_text):
        self.store.set(self.store.get_iter(path), text = new_text)
    
    def OnFocusIn(self, treeview, event):
        self.get_toplevel().acg.connect_group(65535, 0, 0, self.OnPressDelete)
        self.get_toplevel().acg.connect_group(65471, 0, 0, self.OnPressF2)
        
    def OnFocusOut(self, treeview, event):
        acg = self.get_toplevel().acg.disconnect_key(65535,0)
        acg = self.get_toplevel().acg.disconnect_key(65471,0)
    
    def OnPressDelete(self, *args):
        self.remove_selected()
    
    def OnPressF2(self, *args):
        self.edit_selected()
    
    def edit_selected(self):
        path, col = self.get_cursor()
        
        if(path != None):
            self.set_cursor(path, col, start_editing = True)
    
    def remove_selected(self):
        store, paths = self.get_selection().get_selected_rows()
        references = [gtk.TreeRowReference(store, path) for path in paths]
        
        for reference in references:
            path = reference.get_path()
            iter = store.get_iter(path)
            store.remove(iter)
