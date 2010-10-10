# -*- coding: utf-8 -*-
import gtk
from .mainwindow import MainWindow

class BeerCalcApp:
    def __init__(self):
        self.mainwindow = MainWindow()

    def main(self):
        gtk.main()
