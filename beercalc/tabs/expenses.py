# -*- coding: utf-8 -*-
import gtk
import gobject
import pango

class ExpensesTab(gtk.VBox):
    def __init__(self):
        super(type(self), self).__init__()
        self.title = u"Udgifter"
        self.expenseTable = ExpenseTable()
        self.add(self.expenseTable)
        button = gtk.Button(u"Testknap")
        self.add(button)
        self.child_set_property(self.expenseTable, "expand", True)
        self.child_set_property(button, "expand", False)

class ExpenseTable(gtk.ScrolledWindow):
    def __init__(self):
        super(type(self), self).__init__()
        self.expenseTreeView = ExpenseTreeView()
        self.add(self.expenseTreeView)

class ExpenseTreeView(gtk.TreeView):
    def __init__(self):
        self.store = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_STRING)
        for x in range(20):
            self.store.append(("Tuborg"     ,  "423,23 kr."))
            self.store.append(("Guld tuborg", "2342,23 kr."))

        super(type(self), self).__init__(model=self.store)

        self.col1 = gtk.TreeViewColumn(u"Navn")
        self.col2 = gtk.TreeViewColumn(u"Beløb")
        self.col3 = gtk.TreeViewColumn(u"")

        self.append_column(self.col1)
        self.append_column(self.col2)
        self.append_column(self.col3)

        self.cell1 = gtk.CellRendererText()
        self.cell2 = gtk.CellRendererText()
        
        self.cell2.set_property("xalign", 1)
        
        self.col1.pack_start(self.cell1)
        self.col1.add_attribute(self.cell1, 'text', 0)

        self.col2.pack_start(self.cell2)
        self.col2.add_attribute(self.cell2, 'text', 1)
