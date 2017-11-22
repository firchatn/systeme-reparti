import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class acces:
    def __init__(self):
        pass
    def load_interface(self): 

        builder = Gtk.Builder()
        builder.add_from_file("Layout2.glade")
        window = builder.get_object("window1")
        window.connect("delete-event", Gtk.main_quit)
        window.set_default_size(600, 250)

        window.show_all()


        Gtk.main()



