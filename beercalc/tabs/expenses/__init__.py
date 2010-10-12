# -*- coding: utf-8 -*-
import gtk
from .options import OptionsContainer
from .store import ExpenseStore
from .table import ExpenseContainer

class ExpensesTab(gtk.HBox):
    def __init__(self):
        super(type(self), self).__init__()
        self.title = u"Udgifter"
        self.store = ExpenseStore()
        self.expense = ExpenseContainer(self.store)
        self.options = OptionsContainer(self.expense.treeview)
        self.add(self.expense)
        self.add(self.options)
        self.child_set_property(self.expense, "expand", True)
        self.child_set_property(self.options, "expand", False)
