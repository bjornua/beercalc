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
        
        file_item_sub = gtk.Menu()
        self.set_submenu(file_item_sub)

        save = gtk.MenuItem(u"_Gem")
        quit = gtk.MenuItem(u"_Afslut")

        file_item_sub.append(save)
        file_item_sub.append(quit) 

class HelpMenu(gtk.MenuItem):
    def __init__(self):
        super(type(self), self).__init__(u"_Hjælp")
        
        help_item_sub = gtk.Menu()
        self.set_submenu(help_item_sub)
        
        about = gtk.MenuItem(u"_Om BeerCalc")        
        help_item_sub.append(about) 

