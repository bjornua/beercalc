# -*- coding: utf-8 -*-
import gtk
from beercalc.lib.widget import StockButton

class AccountDialog(gtk.Window):
    def __init__(self, toplevel, account):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.set_property("transient-for"  , toplevel                    )
        self.set_property("modal"          , True                        )
        self.set_property("window-position", gtk.WIN_POS_CENTER_ON_PARENT)
        
        form = AccountForm()
        
        self.add(form)

        self.show_all()

class AccountForm(gtk.VBox):
    def __init__(self):
        gtk.VBox.__init__(self)
        cancel_button = CancelButton()
        save_button = SaveButton()
        self.add(save_button)
        self.add(cancel_button)

class SaveButton(StockButton):
    def __init__(self):
        StockButton.__init__(self, u"_Tilføj", gtk.STOCK_ADD)

    def OnClick(self, button):
        AddDialog(self.get_toplevel())
        

class CancelButton(StockButton):
    def __init__(self):
        StockButton.__init__(self, u"_Tilføj", gtk.STOCK_ADD)

    def OnClick(self, button):
        AddDialog(self.get_toplevel())
        


