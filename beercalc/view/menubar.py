# -*- coding: utf-8 -*-
import gtk

class MenuBar(gtk.MenuBar):
    def __init__(self):
        super(type(self), self).__init__()

        self.append(FileMenu())
        self.append(HelpMenu())

class FileMenu(gtk.MenuItem):
    def __init__(self):
        super(type(self), self).__init__(u"_Filer")
        
        self.menu = gtk.Menu()
        self.set_submenu(self.menu)

        save = gtk.MenuItem(u"_Gem")
        quit = gtk.MenuItem(u"_Afslut")

        self.menu.append(save)
        self.menu.append(quit) 

class HelpMenu(gtk.MenuItem):
    def __init__(self):
        super(type(self), self).__init__(u"_Hjælp")
        
        self.menu = gtk.Menu()
        self.set_submenu(self.menu)
        
        about = gtk.MenuItem(u"_Om BeerCalc")        
        self.menu.append(about) 

