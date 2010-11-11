# -*- coding: utf-8 -*-
import gtk
from beercalc.lib.objects import Account, DKK


class AccountTable(gtk.TreeView):
    def __init__(self, store):
        super(type(self), self).__init__(model=store)
        
        self.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        self.store = store

        self.set_property("rules-hint"    , True )
        self.set_property("rubber-banding", True )
        self.set_property("enable-search" , False)
        
        for n, (title, xalign, expand) in enumerate((
            (u"Type"   , 0., False),
            (u"Navn"   , 0., True ),
            (u"Email"  , 0., False),
            (u"Balance", 0., False),
        )):
            coll = gtk.TreeViewColumn()
            cell = gtk.CellRendererText()
            coll.pack_start(cell)
            coll.set_property("title", title)
            coll.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)
            coll.set_property("expand", expand)
            coll.add_attribute(cell, 'text', n+1)
            cell.set_property("xalign", 0)
            self.append_column(coll)

        self.connect("focus-in-event", self.OnFocusIn)
        self.connect("focus-out-event", self.OnFocusOut)
        

    def OnFocusIn(self, treeview, event):
        self.get_toplevel().acg.connect_group(65535, 0, 0, self.OnPressDelete)
        
    def OnFocusOut(self, treeview, event):
        acg = self.get_toplevel().acg.disconnect_key(65535,0)
    
    def OnPressDelete(self, *args):
        self.remove_selected()
    
    def remove_selected(self):
        store, paths = self.get_selection().get_selected_rows()
        references = [gtk.TreeRowReference(store, path) for path in paths]
        
        for reference in references:
            path = reference.get_path()
            iter = store.get_iter(path)
            store.remove(iter)
