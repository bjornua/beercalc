# -*- coding: utf-8 -*-
import gtk
from beercalc.lib.widget import StockButton, InputErrorDialog
from beercalc.lib.objects import Product,DKK
from beercalc.lib import parsenumber

class EditProductDialog(gtk.Window):
    def __init__(self, toplevel, store, product):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.set_property("title"          , u"Ændr produkt"             )
        self.set_property("transient-for"  , toplevel                    )
        self.set_property("modal"          , True                        )
        self.set_property("window-position", gtk.WIN_POS_CENTER_ON_PARENT)
        self.acg = gtk.AccelGroup()
        self.add_accel_group(self.acg)
        form = EditProductForm(store, product)
        self.acg.connect_group(65307, 0, 0, lambda *args: self.destroy())
        self.acg.connect_group(65293, 0, 0, lambda *args: form.button_save.OnClick())
        
        self.add(form)

        self.show_all()

class EditProductForm(gtk.VBox):
    def __init__(self, store, product):
        gtk.VBox.__init__(self)
        
        input          = gtk.Table()
        name_entry     = gtk.Entry()
        sell_val_entry = gtk.Entry()
        buy_val_entry  = gtk.Entry()
        misc_entry     = gtk.Entry()

        buttons       = gtk.HButtonBox()
        button_cancel = CancelButton()
        button_save   = SaveButton(self.get_form_data, store)
        self.button_save = button_save
        
        for parent, child in (
            (self, input),
            (self, buttons),
                (buttons, button_cancel),
                (buttons, button_save),
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
            
            input.attach(
                child = label,
                left_attach = 0,
                right_attach = 1,
                top_attach = n,
                bottom_attach = n + 1,
                ypadding = 5,
                yoptions=gtk.SHRINK|gtk.FILL,
                xoptions=gtk.SHRINK|gtk.FILL
            )
            input.attach(
                child = item,
                left_attach = 1,
                right_attach = 2,
                top_attach = n,
                bottom_attach = n + 1,
                yoptions = gtk.SHRINK,
                xoptions = gtk.FILL|gtk.EXPAND
            )
        
        # Bottom window filler
        input.attach(gtk.HBox(),
            left_attach = 0,
            right_attach = 2,
            top_attach = 4,
            bottom_attach = 5,
            yoptions = gtk.EXPAND|gtk.FILL
        )
        
        input.set_property("column-spacing", 15)
        input.set_property("row-spacing", 4)
        sell_val_entry.set_property("text", "0,00")
        buy_val_entry.set_property("text", "0,00")
        self .set_property("border-width", 10)
        
        self.name_entry     = name_entry
        self.sell_val_entry = sell_val_entry
        self.buy_val_entry  = buy_val_entry
        self.misc_entry     = misc_entry
        
        buttons.set_property("layout-style", gtk.BUTTONBOX_END)
        self.child_set_property(buttons, "expand", False)

    def get_form_data(self):
        name     = self.name_entry    .get_property("text")
        sell_val = self.sell_val_entry.get_property("text")
        buy_val  = self.buy_val_entry .get_property("text")
        misc     = self.misc_entry    .get_property("text")
        
        return name, sell_val, buy_val, misc

class SaveButton(StockButton):
    def __init__(self, data_callback, store):
        StockButton.__init__(self, u"_Tilføj", gtk.STOCK_ADD)
        self.data_callback = data_callback
        self.store = store

    
    def OnClick(self, *args):
        error_messages = list()
        
        name, sell_val, buy_val, misc = self.data_callback()

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
        
        product = Product(
            buy_val = DKK(buy_val),
            sell_val = DKK(sell_val),
            name = name
        )
        
        self.store.append(product)
        self.get_toplevel().destroy()

class CancelButton(StockButton):
    def __init__(self):
        StockButton.__init__(self, u"_Annullér", gtk.STOCK_CANCEL)

    def OnClick(self, button):
        self.get_toplevel().destroy()


