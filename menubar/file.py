# -*- coding: utf-8 -*-
import wx

class FileMenu(wx.Menu):
    def __init__(self, menubar):
        wx.Menu.__init__(self)
        self.menubar = menubar
        self.title = u"&Filer"
        self.open = FileMenuOpen(self)
        self.save = FileMenuSave(self)
        self.saveAs = FileMenuSaveAs(self)
        self.exit = FileMenuExit(self)
        for menuItem in (self.open, self.save, self.saveAs, self.exit):
            self.AppendItem(menuItem)

class FileMenuOpen(wx.MenuItem):
    def __init__(self, menu):
        wx.MenuItem.__init__(self, menu, wx.ID_OPEN, u"&Åbn", u"Åben en fil")

class FileMenuSave(wx.MenuItem):
    def __init__(self, menu):
        wx.MenuItem.__init__(self, menu, wx.ID_SAVE, u"&Gem", u"Gem filen")

class FileMenuSaveAs(wx.MenuItem):
    def __init__(self, menu):
        wx.MenuItem.__init__(self, menu, wx.ID_SAVEAS, u"Gem &som", u"Gem filen som et andet navn")

class FileMenuExit(wx.MenuItem):
    def __init__(self, menu):
        wx.MenuItem.__init__(self, menu, wx.ID_EXIT, u"&Afslut", u"Afslut BeerCalc")
