# -*- coding: utf-8 -*-
import wx

class MainMenuBar(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_OPEN, u"&Åbn", u"Åben en fil")
        filemenu.Append(wx.ID_SAVE, u"&Gem", u"Gemmer filen")
        filemenu.Append(wx.ID_EXIT, u"&Luk", u"Luk BeerCalc")
        self.Append(filemenu, u"&Filer")

class ExpenseTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Udgifter"
        wx.NotebookPage.__init__(self, parent, -1)

class ConfigTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Konfiguration"
        wx.NotebookPage.__init__(self, parent, -1)

class PeopleTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Personer"
        wx.NotebookPage.__init__(self, parent, -1)

class StreglisteTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Stregliste"
        wx.NotebookPage.__init__(self, parent, -1)

class StatusTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Status"
        wx.NotebookPage.__init__(self, parent, -1)

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
        self.SetMenuBar(MainMenuBar())
        self.TabPanel = TabPanel(self)
        self.Show(True)
