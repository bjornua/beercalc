# -*- coding: utf-8 -*-
import wx

class PeopleTab(wx.NotebookPage):
    def __init__(self, parent):
        self.title = u"Personer"
        wx.NotebookPage.__init__(self, parent, -1)
