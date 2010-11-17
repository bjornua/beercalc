# -*- coding: utf-8 -*-

from collections import defaultdict

class Observers(object):
    def __init__(self):
        self.signals = defaultdict(list)
    
    def add(self, signal, callback, *args, **kwargs):
        self.signals[signal].append((callback, args, kwargs))
    
    def notify(self, signal, *notifier_args, **notifier_kwargs):
        for callback, observer_args, observer_kwargs in self.signals[signal]:
            kwargs = dict(notifier_kwargs)
            kwargs.update(observer_kwargs)
            args = observer_args + notifier_args
            callback(*args, **kwargs)

class Observable(object):
    def __init__(self):
        self.observers = Observers()
        object.__init__(self)

def parsenumber(text):
        if not all(x in "0123456789," for x in text):
            return
        text = (text + "00").split(",")
        if len(text) > 2:
            return
        return int("".join(text[0:1]) + "".join(text[1:2])[0:2])
