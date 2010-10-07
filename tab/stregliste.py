# -*- coding: utf-8 -*-
import wx

class StreglisteTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Stregliste"
        wx.NotebookPage.__init__(self, parent, -1)
