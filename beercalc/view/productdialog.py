# -*- coding: utf-8 -*-
import gtk
from .inputerrordialog import InputErrorDialog
from .stockbutton import StockButton
from beercalc.lib import parsenumber, Observable

class ProductDialog(gtk.Window, Observable):
    def __init__(self, toplevel):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        Observable.__init__(self)
        for key, value in (
            ("title"          , u"Opret produkt"),
            ("transient-for"  , toplevel),
            ("modal"          , True),
            ("window-position", gtk.WIN_POS_CENTER_ON_PARENT),
        ):
            self.set_property(key, value)
        
        form = ProductForm()
        form.observers.add("submit", self._OnSubmit)
        form.observers.add("cancel", self._OnCancel)
        acg = gtk.AccelGroup()
        
        # Escape, Enter, Keypad Enter
        for (key, callback) in (
            (65307, form.cancel), # Escape
            (65293, form.submit), # Enter
            (65421, form.submit), # Keypad Enter
        ):
            acg.connect_group(key, 0, 0, lambda *args: callback()) # Escape
        
        self.add_accel_group(acg)
        self.add(form)
        self.show_all()
    
    def _OnSubmit(self, name, sell_val, buy_val, misc):
        self.observers.notify("submit", name, sell_val, buy_val, misc)
        return
        
    def _OnCancel(self):
        self.observers.notify("cancel")
        return
    
    
class ProductForm(gtk.VBox, Observable):
    def __init__(self):
        gtk.VBox.__init__(self)
        Observable.__init__(self)
        
        table          = gtk.Table()
        name_entry     = gtk.Entry()
        sell_val_entry = gtk.Entry()
        buy_val_entry  = gtk.Entry()
        misc_entry     = gtk.Entry()
        buttons        = gtk.HButtonBox()
        button_cancel  = StockButton(u"_Annullér", gtk.STOCK_CANCEL)
        button_submit  = StockButton(u"_Gem", gtk.STOCK_SAVE)

        button_submit.observers.add("clicked", self.submit)
        button_cancel.observers.add("clicked", self.cancel)
        
        for parent, child in (
            (self, table),
            (self, buttons),
                (buttons, button_cancel),
                (buttons, button_submit),
        ):
            parent.add(child)
 
        for (n, (label_text, item)) in enumerate((
            (u"Produktnavn:", name_entry    ),
            (u"Indkøbspris:", buy_val_entry ),
            (u"Salgspris:"  , sell_val_entry),
            (u"Andet:"      , misc_entry    ),
        )):
            label = gtk.Label(label_text)
            label.set_property("xalign", 0.)
            label.set_property("yalign", 0.)
            
            table.attach(
                child = label,
                left_attach = 0,
                right_attach = 1,
                top_attach = n,
                bottom_attach = n + 1,
                ypadding = 5,
                yoptions=gtk.SHRINK|gtk.FILL,
                xoptions=gtk.SHRINK|gtk.FILL
            )
            table.attach(
                child = item,
                left_attach = 1,
                right_attach = 2,
                top_attach = n,
                bottom_attach = n + 1,
                yoptions = gtk.SHRINK,
                xoptions = gtk.FILL|gtk.EXPAND
            )
        
        # Bottom window filler
        table.attach(gtk.HBox(),
            left_attach = 0,
            right_attach = 2,
            top_attach = 4,
            bottom_attach = 5,
            yoptions = gtk.EXPAND|gtk.FILL
        )
        
        
        for widget, key, val in (
            (table         , "column-spacing", 15               ),
            (table         , "row-spacing"   , 4                ),
            (self          , "border-width"  , 10               ),
            (sell_val_entry, "text"          , "0,00"           ),
            (buy_val_entry , "text"          , "0,00"           ),
            (buttons       , "layout-style"  , gtk.BUTTONBOX_END)
        ):
            widget.set_property(key, val)
        
        self.name_entry     = name_entry
        self.sell_val_entry = sell_val_entry
        self.buy_val_entry  = buy_val_entry
        self.misc_entry     = misc_entry
        
        self.child_set_property(buttons, "expand", False)

    def submit(self):
        error_messages = list()
        
        name     = self.name_entry    .get_property("text")
        sell_val = self.sell_val_entry.get_property("text")
        buy_val  = self.buy_val_entry .get_property("text")
        misc     = self.misc_entry    .get_property("text")

        sell_val = parsenumber(sell_val)
        buy_val = parsenumber(buy_val)
        
        if name == "":
            error_messages.append(u"Produktnavn ikke udfyldt")
        if sell_val == None:
            error_messages.append(u"Fejl i salgspris")
        if buy_val == None:
            error_messages.append(u"Fejl i købspris")

        if len(error_messages):
            dialog = InputErrorDialog(error_messages, self.get_toplevel())
            dialog.show_all()
            return 
        
        self.observers.notify("submit", name, sell_val, buy_val, misc)
        self.get_toplevel().destroy()
        
    def cancel(self):
        self.observers.notify("cancel")
        self.get_toplevel().destroy()

