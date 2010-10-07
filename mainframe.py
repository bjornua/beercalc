# -*- coding: utf-8 -*-
import wx
from menubar import MenuBar
from tabpanel import TabPanel

class MainFrame(wx.Frame):
    def __init__(self):
        size = (600,480)
        title = u"BeerCalc"
        wx.Frame.__init__(self, None, title=title, size=size)
        self.CreateStatusBar() # self.GetStatusBar()
        self.SetMenuBar(MenuBar(self)) # self.GetMenuBar()
        self.tabPanel = TabPanel(self)
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

