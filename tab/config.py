# -*- coding: utf-8 -*-
import wx

class ConfigTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Konfiguration"
        wx.NotebookPage.__init__(self, parent, -1)
