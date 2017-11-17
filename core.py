import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import random
 
passToSave = ''

"""
    Class Handler events : Lisente event 
    button of app
"""

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def login(self, butgenerator):
        pass

builder = Gtk.Builder()
builder.add_from_file("Layout.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(600, 500)
window.show_all()


Gtk.main()


