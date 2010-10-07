# -*- coding: utf-8 -*-
import wx
from mainframe import MainFrame

class BeerCalcApp(wx.App):
    def __init__(self):
        wx.App.__init__(self, False)
        MainFrame()
