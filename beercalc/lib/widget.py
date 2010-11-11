# -*- coding: utf-8 -*-
import gtk

class StockButton(gtk.Button):
    def __init__(self, label, stock_image):
        gtk.Button.__init__(self, label)
        self.image = gtk.Image()
        self.image.set_from_stock(stock_image, gtk.ICON_SIZE_MENU)
        self.set_image(self.image)
        self.connect("clicked", self.OnClick)


class InputErrorDialog(gtk.MessageDialog):
    def __init__(self, errors, toplevel):
        errors.insert(0, u"<b>Fejl:</b>")
        error_message = "\n  ∘ ".join(errors)
        gtk.MessageDialog.__init__(self,
            parent = toplevel,
            flags = gtk.DIALOG_MODAL,
            type = gtk.MESSAGE_ERROR,
            buttons = gtk.BUTTONS_OK,
            message_format = error_message
        )
        self.set_property("use-markup", True)
        self.connect("response", lambda *args: self.hide())

