# -*- coding: utf-8 -*-
import gtk
import gobject
import pango

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
        self.button_edit = EditButton()
        self.add(self.button_add)
        self.add(self.button_remove)
        self.add(self.button_edit)
        self.child_set_property(self.button_add, "expand", False)
        self.child_set_property(self.button_remove, "expand", False)
        self.child_set_property(self.button_edit, "expand", False)

class AddButton(gtk.Button):
    def __init__(self):
        super(type(self), self).__init__(u"_Tilføj")
        
class RemoveButton(gtk.Button):
    def __init__(self):
        super(type(self), self).__init__(u"_Slet")
        self.connect("clicked", self.OnClick)
    
    def OnClick(self, button):
        table = self.get_parent().get_parent().expenseTable.table
        selection = list(table.get_selection().get_selected())[1]
        
        if selection != None:
            raise Exception(selection)
        
class EditButton(gtk.Button):
    def __init__(self):
        super(type(self), self).__init__(u"_Redigér")

class ExpenseTable(gtk.ScrolledWindow):
    def __init__(self):
        super(type(self), self).__init__()
        self.table = ExpenseTreeView()
        self.add(self.table)

class ExpenseTreeView(gtk.TreeView):
    def __init__(self):
        self.store = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_STRING)
        self.store.append(("Tuborg"     ,  "423,23 kr."))
        self.store.append(("Guld tuborg", "2342,23 kr."))
        self.store.append(("Sodavand",       "3,23 kr."))

        super(type(self), self).__init__(model=self.store)
        
        self.set_property("rules-hint"   , True)
        
        self.set_property("enable-search", True)
        self.set_property("search-column", 0   )
        
        self.col1 = gtk.TreeViewColumn()
        self.col2 = gtk.TreeViewColumn()

        self.cell1 = gtk.CellRendererText()
        self.cell2 = gtk.CellRendererText()
        
        self.col1.pack_start(self.cell1, expand=True)
        self.col2.pack_start(self.cell2, expand=False)
        
        self.col1.set_property("title", u"Beskrivelse")
        self.col1.set_property("expand", True)
        self.cell1.set_property("xalign", 0)

        self.col2.set_property("title", u"Pris")
        self.cell2.set_property("xalign", 1)
        
        self.col1.add_attribute(self.cell1, 'text', 0)
        self.col2.add_attribute(self.cell2, 'text', 1)
        
        self.append_column(self.col1)
        self.append_column(self.col2)

