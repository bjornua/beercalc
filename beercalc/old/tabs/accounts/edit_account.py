# -*- coding: utf-8 -*-
import gtk
from beercalc.lib.widget import StockButton, InputErrorDialog
from beercalc.lib.objects import Account,DKK
from beercalc.lib import parsenumber

class AccountDialog(gtk.Window):
    def __init__(self, toplevel, store):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.set_property("title"          , u"Opret produkt"            )
        self.set_property("transient-for"  , toplevel                    )
        self.set_property("modal"          , True                        )
        self.set_property("window-position", gtk.WIN_POS_CENTER_ON_PARENT)
        self.acg = gtk.AccelGroup()
        self.add_accel_group(self.acg)
        form = AccountForm(store)
        self.acg.connect_group(65307, 0, 0, lambda *args: self.destroy())
        self.acg.connect_group(65293, 0, 0, lambda *args: form.button_save.OnClick())
        self.acg.connect_group(65421, 0, 0, lambda *args: form.button_save.OnClick())

        self.add(form)

        self.show_all()

class AccountForm(gtk.VBox):
    def __init__(self, store):
        gtk.VBox.__init__(self)
        
        input         = gtk.Table()
        name_entry    = gtk.Entry()
        email_entry   = gtk.Entry()
        type_vbox     = gtk.VBox()
        type_rus      = gtk.RadioButton(label=u"_Rus")
        type_vejleder = gtk.RadioButton(group = type_rus, label=u"_Rusvejleder")
        misc_entry    = gtk.Entry()

        buttons       = gtk.HButtonBox()
        button_cancel = CancelButton()
        button_save   = SaveButton(self.get_form_data, store)
        self.button_save = button_save
        
        for parent, child in (
            (self, input),
            (self, buttons),
                (buttons, button_cancel),
                (buttons, button_save),
            (type_vbox, type_rus),
            (type_vbox, type_vejleder),
        ):
            parent.add(child)
 
        for (n, (label_text, item)) in enumerate((
            (u"Kontonavn:", name_entry ),
            (u"Email:"    , email_entry),
            (u"Type:"     , type_vbox ),
            (u"Andet:"    , misc_entry ),
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
        self .set_property("border-width", 10)
        
        self.name_entry    = name_entry
        self.email_entry   = email_entry
        self.type_rus      = type_rus
        self.type_vejleder = type_vejleder
        self.misc_entry    = misc_entry
        
        buttons.set_property("layout-style", gtk.BUTTONBOX_END)
        self.child_set_property(buttons, "expand", False)

    def get_form_data(self):
        name  = self.name_entry.get_property("text")
        email = self.email_entry.get_property("text")
        if self.type_rus.get_property("active"):
            type = "rus"
        else:
            type = "rusvejleder"
        misc = self.misc_entry .get_property("text")
        
        return name, email, type, misc

class SaveButton(StockButton):
    def __init__(self, data_callback, store):
        StockButton.__init__(self, u"_Tilføj", gtk.STOCK_ADD)
        self.data_callback = data_callback
        self.store = store

    def OnClick(self, *args):
        error_messages = list()
        
        name, email, type, misc = self.data_callback()

        if name == "":
            error_messages.append(u"Navn ikke udfyldt")
        if email == "":
            email = None
        if misc == "":
            misc = None
        
        if len(error_messages):
            dialog = InputErrorDialog(error_messages, self.get_toplevel())
            dialog.show_all()
            return 
        
        account = Account(
            name = name,
            email = email,
            type = type,
            misc = misc
        )
        
        self.store.append(account)
        self.get_toplevel().destroy()

class CancelButton(StockButton):
    def __init__(self):
        StockButton.__init__(self, u"_Annullér", gtk.STOCK_CANCEL)

    def OnClick(self, button):
        self.get_toplevel().destroy()
