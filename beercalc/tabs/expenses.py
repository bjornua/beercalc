# -*- coding: utf-8 -*-
import gtk
import gobject
import pango
import uuid

class ExpensesTab(gtk.HBox):
    def __init__(self):
        super(type(self), self).__init__()
        self.title = u"Udgifter"
        self.expenseTable = ExpenseTable()
        self.optionsContainer = OptionsContainer()
        self.add(self.expenseTable)
        self.add(self.optionsContainer)
        self.child_set_property(self.expenseTable, "expand", True)
        self.child_set_property(self.optionsContainer, "expand", False)

class OptionsContainer(gtk.VBox):
    def __init__(self):
        super(type(self), self).__init__()
        self.button_add = AddButton()
        self.button_remove = RemoveButton()
        self.add(self.button_add)
        self.add(self.button_remove)
        self.child_set_property(self.button_add, "expand", False)
        self.child_set_property(self.button_remove, "expand", False)


class ExpenseTable(gtk.ScrolledWindow):
    def __init__(self):
        super(type(self), self).__init__()
        self.table = ExpenseTreeView()
        self.add(self.table)

class ExpenseTreeView(gtk.TreeView):
    def __init__(self):
        self.store = gtk.ListStore(gobject.TYPE_PYOBJECT, gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_PYOBJECT)

        super(type(self), self).__init__(model=self.store)
        
        self.set_property("rules-hint"   , True)
        
        self.set_property("enable-search", True)
        self.set_property("search-column", 1   )
        
        self.col1 = gtk.TreeViewColumn()
        self.col2 = gtk.TreeViewColumn()

        self.cell1 = gtk.CellRendererText()
        self.cell2 = AmountCell(self)

        self.col1.pack_start(self.cell1, expand=True)
        self.col2.pack_start(self.cell2, expand=False)
        
        self.cell1.connect("edited", self.OnEditDoneDesc)
        
        self.col1.set_property("title", u"Beskrivelse")
        self.col1.set_property("expand", True)
        self.col1.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)
        self.cell1.set_property("xalign", 0)

        self.col2.set_property("title", u"Pris")
        self.col2.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)

        self.cell1.set_property("editable", True)
        
        self.col1.add_attribute(self.cell1, 'text', 1)
        self.col2.add_attribute(self.cell2, 'text', 2)
        
        self.append_column(self.col1)
        self.append_column(self.col2)

    def OnEditDoneDesc(self, cell, path, new_text):
        iter = self.store.get_iter(path)
        self.store.set(iter, 1, new_text)


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

    def OnEditEnd(self, cell, path, new_text):
        new_text = new_text + "00"
        if not all(x in "0123456789," for x in new_text):
            return
        
        new_text = new_text.split(",")
        if len(new_text) > 2:
            return
        amount = int("".join(new_text[0:1]) + "".join(new_text[1:2])[0:2])
        
        integer  = str(amount / 100)
        fraction = str(amount % 100)
        fraction = (fraction + "0")[:2]
        
        new_text = integer + "," + fraction + " kr."
        
        store = self.treeview.store
        iter = store.get_iter(path)
        store.set(iter, 2, new_text, 3, amount)


class AddButton(gtk.Button):
    def __init__(self):
        super(type(self), self).__init__(u"_Tilføj")
        self.connect("clicked", self.OnClick)

    def OnClick(self, button):
        table = self.get_parent().get_parent().expenseTable.table
        iter = table.store.append((uuid.uuid4().get_hex(), "", "0,00 kr.", 0))
        table.set_cursor(table.store.get_path(iter), table.col1, True)

class RemoveButton(gtk.Button):
    def __init__(self):
        super(type(self), self).__init__(u"_Slet")
        self.connect("clicked", self.OnClick)
    
    def OnClick(self, button):
        table = self.get_parent().get_parent().expenseTable.table
        selection = list(table.get_selection().get_selected())
        
        if selection[1] != None:
            treeStore, iter = selection
            selection = treeStore.remove(iter)
