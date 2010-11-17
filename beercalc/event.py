# -*- coding: utf-8 -*-
import gtk
from beercalc.lib.types import DKK
from beercalc.model.product import Product

from beercalc.lib import Observers


def quit():
    gtk.main_quit()


def add_product(mainwindow, products, name, sell_val, buy_val, misc):
    if misc == "":
        misc = None
    product = Product(DKK(sell_val), DKK(buy_val), name, misc = misc)
    products.add(product)
    
    def name(col_updater):
        def send(*args): col_updater(str(product.name))
        product.observers.add("changed(name)", send)
        send()
    def count(col_updater):
        def send(*args):
            if product.count == None:
                col_updater("")
            else:
                col_updater(str(product.count))
        product.observers.add("changed(count)", send)
        send()
    def buy_val(col_updater):
        def send(*args): col_updater(str(product.buy_val))
        product.observers.add("changed(buy_val)", send)
        send()
    def sell_val(col_updater):
        def send(*args): col_updater(str(product.sell_val))
        product.observers.add("changed(sell_val)", send)
        send()
    
    def remove():
        products.discard(product)
    
        
    def edit():
        mainwindow.product_dialog(product.name, product.sell_val, product.buy_val, product.misc)

    observers = Observers()
    observers.add("remove", remove)
    observers.add("edit", edit)
        
    
    mainwindow.add_product((name, count, buy_val, sell_val), observers)

