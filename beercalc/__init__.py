# -*- coding: utf-8 -*-
import gtk

from beercalc.view.mainwindow import MainWindow
import beercalc.event as event

class BeerCalcApp:
    def __init__(self):
        products = set()
        mainwindow = MainWindow()
        
        mainwindow.observers.add("quit", event.quit)
        mainwindow.observers.add("add_product", event.add_product, mainwindow, products)
        event.add_product(mainwindow, products, "Tuborg Guld", 40000, 0, "")
        event.add_product(mainwindow, products, "Grøn Tuborg", 43200, 0, "")
        
        
    def main(self):
        gtk.main()

