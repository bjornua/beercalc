#!/usr/bin/env python
import gtk
def catch_button(window, event, label):
        keyval = event.keyval
        name = gtk.gdk.keyval_name(keyval)
        print event.state
        mod = gtk.accelerator_get_label(keyval,event.state)
        label.set_markup('<span size="xx-large">%s\n%d</span>'% (mod, keyval)) 


window = gtk.Window()
window.set_size_request(640,480)
label = gtk.Label()
label.set_use_markup(True)
window.connect('key-press-event',catch_button, label)
window.connect('destroy', gtk.main_quit)
window.add(label)
window.show_all()
gtk.main()
