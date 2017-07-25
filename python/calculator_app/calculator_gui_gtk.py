#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class CalculatorWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Calculator Gtk v.0.3")
        self.connect("destroy", Gtk.main_quit)
        #self.connect("delete-event", Gtk.main_quit)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Entry
        self.entry = Gtk.Entry()
        self.entry.set_hexpand(True)
        self.entry.set_vexpand(True)
        self.entry.set_alignment(1.0)
        
        # Buttons
        self.buttons = []
        self.add_buttons()
        self.arrange_buttons()


    def add_buttons(self):
        self.buttons.append(Gtk.Button(label="1"))
        self.buttons.append(Gtk.Button(label="2"))
        self.buttons.append(Gtk.Button(label="3"))
        self.buttons.append(Gtk.Button(label="4"))
        self.buttons.append(Gtk.Button(label="5"))
        self.buttons.append(Gtk.Button(label="6"))
        self.buttons.append(Gtk.Button(label="7"))
        self.buttons.append(Gtk.Button(label="8"))
        self.buttons.append(Gtk.Button(label="9"))
        self.buttons.append(Gtk.Button(label="0"))
        self.buttons.append(Gtk.Button(label="."))
        self.buttons.append(Gtk.Button(label="+"))
        self.buttons.append(Gtk.Button(label="-"))
        self.buttons.append(Gtk.Button(label="*"))
        self.buttons.append(Gtk.Button(label="/"))
        self.buttons.append(Gtk.Button(label="="))

    
    def arrange_buttons(self):
        # Compose GUI
        #  attach(child, left, top, (span) width, height)
        self.grid.set_column_homogeneous(True)
        self.grid.attach(self.entry, 0, 0, 6, 1)
        self.entry.connect('key_press_event', self.on_key_press_event)

        # Row 1
        self.attach_button("1", 0, 1, 1, 1)
        self.attach_button("2", 1, 1, 1, 1)
        self.attach_button("3", 2, 1, 1, 1)
        self.attach_button("+", 4, 1, 1, 1)
        self.attach_button("=", 5, 1, 1, 4)

        # Row 2
        self.attach_button("4", 0, 2, 1, 1)
        self.attach_button("5", 1, 2, 1, 1)
        self.attach_button("6", 2, 2, 1, 1)
        self.attach_button("-", 4, 2, 1, 1)

        # Row 3
        self.attach_button("7", 0, 3, 1, 1)
        self.attach_button("8", 1, 3, 1, 1)
        self.attach_button("9", 2, 3, 1, 1)
        self.attach_button("*", 4, 3, 1, 1)

        # Row 4
        self.attach_button("0", 0, 4, 1, 1)
        self.attach_button(".", 1, 4, 1, 1)
        self.attach_button("/", 4, 4, 1, 1)
    

    def attach_button(self, button_label, left, top, span_width, span_height):
        # if button_label is "empty":
        #     print('Adding empty space')
        #     empty_label = Gtk.Label(label="")
        #     empty_label.set_hexpand(True)
        #     empty_label.set_vexpand(True)
        #     self.grid.attach(empty_label, left, top, span_width, span_height)
        #     return
        for button in self.buttons:
            if button.get_label() is button_label:
                print('Adding button '+ button_label)
                button.set_hexpand(True)
                button.set_vexpand(True)
                self.grid.attach(button, left, top, span_width, span_height)
                button.connect("clicked", self.on_click_button)
                button.connect('key_press_event', self.on_key_press_event)
                return


    def on_click_button(self, button):
        print("Button %s was clicked" % (button.get_label()))
        self.entry.set_text(self.entry.get_text()+button.get_label())
    

    def on_key_press_event(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)
        print("Key %s (%d) was pressed" % (keyname, event.keyval))
        self.entry.set_text(self.entry.get_text()+keyname)


def main():
    calc_win = CalculatorWindow()
    calc_win.show_all()
    Gtk.main()
    return 0

if __name__ == "__main__":
    main()
