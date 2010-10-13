# -*- coding: utf-8 -*-
import gtk

class ExpenseContainer(gtk.VBox):
    def __init__(self, store):
        super(type(self), self).__init__()
        self.scrollwindow = ExpenseTableScroll(store)
        self.status = ExpenseStatus()
        self.add(self.scrollwindow)
        self.add(self.status)
        self.child_set_property(self.status, "expand", False)

class ExpenseStatus(gtk.HBox):
    def __init__(self):
        super(type(self), self).__init__()
        self.label = gtk.Label()
        self.update_amount(0)
        self.label.set_property("xalign", 1)
        self.add(self.label)
    
    def update_amount(self, amount):
        integer  = str(amount // 100)
        fraction = str(amount % 100)
        fraction = (fraction + "0")[:2]
        integer = integer[::-1]
        integer = ".".join(integer[i:i+3] for i in range(0, len(integer), 3))
        integer = integer[::-1]
        amount_text = integer + "," + fraction + " kr."
        
        self.label.set_markup(u"Total: <b>" + amount_text + "</b>")

class ExpenseTableScroll(gtk.ScrolledWindow):
    def __init__(self, store):
        super(type(self), self).__init__()
        self.treeview = ExpenseTable(store)
        self.set_property("vscrollbar-policy", gtk.POLICY_ALWAYS)
        self.set_property("hscrollbar-policy", gtk.POLICY_NEVER)
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
        self.update_status()
    
    def append_new(self):
        iter = self.store.append_new()
        self.update_status()
        path = self.store.get_path(iter)
        self.set_cursor(path, self.col_desc, start_editing = True)
    
    def update_status(self):
        self.get_parent().get_parent().status.update_amount(self.store.total)

class AmountCell(gtk.CellRendererText):
    def __init__(self, treeview):
        super(type(self), self).__init__()
        self.treeview = treeview
        self.set_property("xalign", 1)
        self.connect("edited", self.OnEditEnd)
        self.connect("editing-started", self.OnEditStart)
        self.set_property("editable", True)
    
    def OnEditStart(self, cell, entry, path):
        amount = self.treeview.store[path][1]
        integer  = str(amount // 100)
        fraction = str(amount % 100)
        fraction = (fraction + "0")[:2]
        amount_text = integer + "," + fraction
        entry.set_text(amount_text)

    def OnEditEnd(self, cell, path, amount):
        if not all(x in "0123456789," for x in amount):
            return
        amount = (amount + "00").split(",")
        if len(amount) > 2:
            return
        amount = int("".join(amount[0:1]) + "".join(amount[1:2])[0:2])

        store = self.treeview.store
        store.set(store.get_iter(path), amount = amount)
        self.treeview.update_status()

