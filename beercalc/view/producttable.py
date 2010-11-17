# -*- coding: utf-8 -*-
import gobject
import gtk

from beercalc.lib.types import DKK
from beercalc.lib import Observable

class ProductTable(gtk.TreeView, Observable):
    def __init__(self):
        self.store = StringStore(4)
        gtk.TreeView.__init__(self, model=self.store)
        Observable.__init__(self)
        self.get_selection().set_mode(gtk.SELECTION_SINGLE)

        self.set_property("rules-hint"   , True)
        self.set_property("enable-search", False)
        
        for n, (title, xalign, expand) in enumerate((
            (u"Beskrivelse"        , 0., True ),
            (u"Antal"              , 1., False),
            (u"Indkøbspris (total)", 1., False),
            (u"Salgspris (total)"  , 1., False),
        )):
            coll = gtk.TreeViewColumn()
            cell = gtk.CellRendererText()
            coll.pack_start(cell)
            coll.set_property("title", title)
            coll.set_property("sizing", gtk.TREE_VIEW_COLUMN_AUTOSIZE)
            coll.set_property("expand", expand)
            coll.add_attribute(cell, 'text', n)
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
    
    def add_row(self, cols, observers):
        self.store.add_row(cols, observers)
    
    def remove_selection(self):
        model, paths = self.get_selection().get_selected_rows()
        self.store.remove_rows(paths)
    
class StringStore(gtk.ListStore, Observable):
    def __init__(self, colcount):
        cols = [gobject.TYPE_STRING for _ in range(colcount)]
        cols += [gobject.TYPE_PYOBJECT]
        self.colcount = colcount
        gtk.ListStore.__init__(self, *cols)
        Observable.__init__(self)

    def add_row(self, cols, observer):
        iter_ = self.append()
        path = self.get_path(iter_)
        ref = gtk.TreeRowReference(self, path)
        for n, col in enumerate(cols):
            def update_col(content): self[ref.get_path()][n] = content
            col(update_col)
        self[iter_][self.colcount] = observers
    
    def remove_row(self, ref):
        path = ref.get_path()
        iter_ = self.get_iter(path)
        deleted = self[iter_][self.colcount][0]
        self.remove(iter_)
        deleted()
    
    def remove_rows(self, paths):
        for ref in [gtk.TreeRowReference(self, x) for x in paths]:
            self.remove_row(ref)
