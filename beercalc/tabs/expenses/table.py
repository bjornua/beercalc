# -*- coding: utf-8 -*-
import gtk

class ExpenseContainer(gtk.ScrolledWindow):
    def __init__(self, store):
        super(type(self), self).__init__()
        self.treeview = ExpenseTable(store)
        self.add(self.treeview)

class ExpenseTable(gtk.TreeView):
    def __init__(self, store):
        super(type(self), self).__init__(model=store)
        
        self.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        self.store = store

        self.set_property("rules-hint"   , True)
        self.set_property("rubber-banding"   , True)
        
        self.set_property("enable-search", False)
        
        self.col_desc = gtk.TreeViewColumn()
        self.col_amount = gtk.TreeViewColumn()

        self.cell_desc = gtk.CellRendererText()
        self.cell_amount = AmountCell(self)

        self.col_desc.pack_start(self.cell_desc)
        self.col_amount.pack_start(self.cell_amount)
        
        self.col_desc.set_property("title", u"Beskrivelse")
        self.col_desc.set_property("expand", True)
        self.col_desc.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)

        self.col_amount.set_property("title", u"Pris")
        self.col_amount.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)

        self.cell_desc.set_property("xalign", 0)
        self.cell_desc.set_property("editable", True)
        self.cell_desc.connect("edited", self.OnEditDoneDesc)
        
        self.col_desc.add_attribute(self.cell_desc, 'text', 2)
        self.col_amount.add_attribute(self.cell_amount, 'text', 3)
        
        self.append_column(self.col_desc)
        self.append_column(self.col_amount)

        self.connect("focus-in-event", self.OnFocusIn)
        self.connect("focus-out-event", self.OnFocusOut)

    def OnEditDoneDesc(self, cell, path, new_text):
        self.store.set(self.store.get_iter(path), text = new_text)
    
    def OnFocusIn(self, treeview, event):
        acg = self.get_toplevel().acg.connect_group(65535, 0, 0, self.OnPressDelete)
        
    def OnFocusOut(self, treeview, event):
        acg = self.get_toplevel().acg.disconnect_key(65535,0)
    
    def OnPressDelete(self, *args):
        self.remove_selected()
    
    def remove_selected(self):
        store, paths = self.get_selection().get_selected_rows()
        references = [gtk.TreeRowReference(store, path) for path in paths]
        
        for reference in references:
            path = reference.get_path()
            iter = store.get_iter(path)
            store.remove(iter)

class AmountCell(gtk.CellRendererText):
    def __init__(self, treeview):
        super(type(self), self).__init__()
        self.treeview = treeview
        self.set_property("xalign", 1)
        self.connect("edited", self.OnEditEnd)
        self.connect("editing-started", self.OnEditStart)
        self.set_property("editable", True)
    
    def OnEditStart(self, cell, entry, path):
        text = entry.get_text()
        text = text[:-4]
        entry.set_text(text)

    def OnEditEnd(self, cell, path, amount):
        if not all(x in "0123456789," for x in amount):
            return
        amount = (amount + "00").split(",")
        if len(amount) > 2:
            return
        amount = int("".join(amount[0:1]) + "".join(amount[1:2])[0:2])
        
        store = self.treeview.store
        store.set(store.get_iter(path), amount = amount)
