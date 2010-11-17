# -*- coding: utf-8 -*-
import gtk

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
