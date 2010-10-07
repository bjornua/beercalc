# -*- coding: utf-8 -*-
from expense import ExpenseTab
from config import ConfigTab
from people import PeopleTab
from stregliste import StreglisteTab
from status import StatusTab

import wx
class TabPanel(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        self.expenseTab = ExpenseTab(self)
        self.configTab = ConfigTab(self)
        self.peopleTab = PeopleTab(self)
        self.streglisteTab = StreglisteTab(self)
        self.statusTab = StatusTab(self)
        for tab in (self.expenseTab, self.configTab, self.peopleTab, self.streglisteTab, self.statusTab):
            self.AddPage(tab, tab.title)

        self.Layout()
