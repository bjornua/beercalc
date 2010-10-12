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
        
        self.store = store

        self.set_property("rules-hint"   , True)
        
        self.set_property("enable-search", True)
        self.set_property("search-column", 1   )
        
        self.col_desc = gtk.TreeViewColumn()
        self.col_amount = gtk.TreeViewColumn()

        self.cell_desc = gtk.CellRendererText()
        self.cell_amount = AmountCell(self)

        self.col_desc.pack_start(self.cell_desc, expand=True)
        self.col_amount.pack_start(self.cell_amount, expand=False)
        
        self.cell_desc.connect("edited", self.OnEditDoneDesc)
        
        self.col_desc.set_property("title", u"Beskrivelse")
        self.col_desc.set_property("expand", True)
        self.col_desc.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)
        self.cell_desc.set_property("xalign", 0)

        self.col_amount.set_property("title", u"Pris")
        self.col_amount.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)

        self.cell_desc.set_property("editable", True)
        
        self.col_desc.add_attribute(self.cell_desc, 'text', 2)
        self.col_amount.add_attribute(self.cell_amount, 'text', 3)
        
        self.append_column(self.col_desc)
        self.append_column(self.col_amount)

    def OnEditDoneDesc(self, cell, path, new_text):
        self.store.set(self.store.get_iter(path), text = new_text)


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
