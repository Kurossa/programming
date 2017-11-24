#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from calculator_source import CalculatorEngine

class CalculatorWindow(Gtk.Window):

    def __init__(self, calculator_engine ):
        self.calculator_engine = calculator_engine
        Gtk.Window.__init__(self, title="Calculator Gtk v.0.6")
        self.connect("destroy", Gtk.main_quit)
        #self.connect("delete-event", Gtk.main_quit)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Entry
        self.label = Gtk.Label()
        self.label.set_hexpand(True)
        self.label.set_vexpand(True)
        self.label.set_alignment(1.0, 1.0)
        self.label.set_markup("<big>0</big>")

        # Buttons
        self.buttons = []
        self.add_buttons()
        self.arrange_buttons()

        # Keyval dictionary
        self.keys_accepted = '1234567890.+-*/=c'
        self.keys_dict = {'KP_1' : '1',
                          'KP_2' : '2',
                          'KP_3' : '3',
                          'KP_4' : '4',
                          'KP_5' : '5',
                          'KP_6' : '6',
                          'KP_7' : '7',
                          'KP_8' : '8',
                          'KP_9' : '9',
                          'KP_0' : '0',
                          'equal' : '=',
                          'KP_Divide' : '/',
                          'KP_2': '2',
                          'KP_Multiply': '*',
                          'KP_Add': '+',
                          'KP_Subtract': '-',
                          'KP_Enter': '=',
                          'KP_Separator' : '.',
                          'plus' : '+',
                          'minus' : '-',
                          'asteriks' : '*',
                          'slash' : '/',
                          'equal' : '='}


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
        self.buttons.append(Gtk.Button(label="c"))

    
    def arrange_buttons(self):
        # Compose GUI
        #  attach(child, left, top, (span) width, height)
        self.grid.set_column_homogeneous(True)
        self.grid.attach(self.label, 0, 0, 6, 1)
        self.label.connect('key_press_event', self.on_key_press_event)

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
        self.attach_button("c", 2, 4, 1, 1)
        self.attach_button("/", 4, 4, 1, 1)
    

    def attach_button(self, button_label, left, top, span_width, span_height):
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
        result = self.calculator_engine.chars_process(button.get_label())
        print("Button %s was clicked" % (button.get_label()))
        self.label.set_markup("<big>" + result + "</big>")
    

    def on_key_press_event(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)
        print("Key %s (%d) was pressed" % (keyname, event.keyval))
        if  keyname in self.keys_accepted:
            print("Key %s (%d) was pressed" % (keyname, event.keyval))
            result = self.calculator_engine.chars_process(keyname)
            self.label.set_markup("<big>" + result + "</big>")
        elif keyname in self.keys_dict.keys():
            print("Key %s (%d) was pressed" % (self.keys_dict[keyname], event.keyval))
            result = self.calculator_engine.chars_process(self.keys_dict[keyname])
            self.label.set_markup("<big>" + result + "</big>")



def main():
    calc_engine = CalculatorEngine()
    calc_win = CalculatorWindow(calc_engine)
    calc_win.show_all()
    Gtk.main()
    return 0

if __name__ == "__main__":
    main()
