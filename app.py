# -*- coding: utf-8 -*-
import wx
from beercalc.mainframe import MainFrame

class BeerCalcApp(wx.App):
    def __init__(self):
        wx.App.__init__(self, False)
        MainFrame()
