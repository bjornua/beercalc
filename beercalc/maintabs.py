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
        self.append_page(self.expensesTab, gtk.Label(self.expensesTab.title))
        self.append_page(self.configTab, gtk.Label(self.configTab.title))
        self.append_page(self.peopleTab, gtk.Label(self.peopleTab.title))
        self.append_page(self.streglisteTab, gtk.Label(self.streglisteTab.title))
        self.append_page(self.statusTab, gtk.Label(self.statusTab.title))

