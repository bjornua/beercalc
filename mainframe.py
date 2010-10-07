# -*- coding: utf-8 -*-
import wx
from menubar import MenuBar
from tab.expense import ExpenseTab
from tab.config import ConfigTab
from tab.people import PeopleTab
from tab.stregliste import StreglisteTab
from tab.status import StatusTab

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
        
class MainFrame(wx.Frame):
    def __init__(self):
        size = (600,480)
        title = u"BeerCalc"
        wx.Frame.__init__(self, None, title=title, size=size)
        self.CreateStatusBar()
        self.menubar = MenuBar(self)
        self.SetMenuBar(self.menubar)
        self.TabPanel = TabPanel(self)
        self.Show(True)
        self.Bind(wx.EVT_MENU, self.EventHandler)
    
    def EventHandler(self, event):
        if event.Id == wx.ID_OPEN:
            return self.OnOpen()
        if event.Id == wx.ID_EXIT:
            return self.OnExit()
        if event.Id == wx.ID_SAVE:
            return self.OnSave()

    def OnExit(self):
        self.Close(True)

