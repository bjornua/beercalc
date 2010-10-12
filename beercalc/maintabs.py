# -*- coding: utf-8 -*-
import gtk

from .tabs.expenses import ExpensesTab
from .tabs.config import ConfigTab
from .tabs.people import PeopleTab
from .tabs.stregliste import StreglisteTab
from .tabs.status import StatusTab

class MainTabs(gtk.Notebook):
    def __init__(self):
        super(type(self), self).__init__()
        self.expensesTab = ExpensesTab()
        self.configTab = ConfigTab()
        self.peopleTab = PeopleTab()
        self.streglisteTab = StreglisteTab()
        self.statusTab = StatusTab()
        
        for x in (self.expensesTab, self.configTab, self.peopleTab, self.streglisteTab, self.statusTab):
            self.append_page(x, gtk.Label(x.title))
