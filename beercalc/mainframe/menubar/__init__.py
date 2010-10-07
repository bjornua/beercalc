# -*- coding: utf-8 -*-
import wx
from .file import FileMenu

class MenuBar(wx.MenuBar):
    def __init__(self, frame):
        wx.MenuBar.__init__(self)
        self.frame = frame
        self.file = FileMenu(self)
        self.Append(self.file, self.file.title)
