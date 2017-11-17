import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import random
 
passToSave = ''

"""
    Class Handler events
    button of app
"""

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def login(self, login):
        print("login button clicked")
        feedback.set_text("Invalid Username or Password!")
        
        
        
    def clear(self, clear):
        print("clear button clicked")
        feedback.set_text("")
        
    def createUser(self, create):
        print("creating new account")


builder = Gtk.Builder()
builder.add_from_file("Layout.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(600, 250)
inputuser = builder.get_object("entry1")
inputpass = builder.get_object("entry2")
feedback = builder.get_object("label3")
window.show_all()


Gtk.main()


