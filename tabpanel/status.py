# -*- coding: utf-8 -*-
import wx

class StatusTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Status"
        wx.NotebookPage.__init__(self, parent, -1)
