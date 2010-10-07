# -*- coding: utf-8 -*-
import wx

class ExpenseTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Udgifter"
        wx.NotebookPage.__init__(self, parent, -1)
