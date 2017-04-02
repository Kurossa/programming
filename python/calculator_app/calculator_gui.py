#!/usr/bin/python3
import sys
import curses
from curses.textpad import Textbox, rectangle
import calculator_engine
from time import sleep

CALC_TITLE = 'Calculator v0.6'
CALC_WIDTH = 44
CALC_HEIGHT = 20
DISP_WIDTH = 42
DISP_LINES = 4
#TIMEOUT = 100
ALLOWED_NUMBERS = '0123456789.'
ALLOWED_FUNCTIONS = '+-*/='
ALLOWED_CHARACTERS = ALLOWED_NUMBERS + ALLOWED_FUNCTIONS


def filter_char(char, allowed_chars):
    for c in allowed_chars:
        if c == char:
            return c
    return ''


def init_curses():
    curses.initscr()
    curses.beep()
    curses.beep()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.noecho()
    curses.curs_set(0)


class MainWindow(object):
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.window = curses.newwin(self.height, self.width, 0, 0)
        # self.window.timeout(TIMEOUT)
        self.window.keypad(1)
        self.render()

    def render(self):
        # self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 2, self.title, curses.color_pair(1))
        self.window.refresh()

    @property
    def getWindow(self):
        return self.window


class DisplayWindow(object):
    def __init__(self, line_number, width, offset_x, offset_y):
        self.TITLE = 'Result'
        self.WIDTH = width
        self.height = line_number + 2
        self.pos_x = offset_x + 1
        self.pos_y = offset_y + 1
        self.lines = line_number
        self.textLines = ['' for x in range(self.lines)]
        # for i in range(self.lines):
        #     self.textLines = '0'
        self.window = curses.newwin(self.height, self.WIDTH, self.pos_y, self.pos_x)
        self.render()

    def render(self):
        self.window.clear()
        self.window.border(0)
        i = 0
        for text in self.textLines:
            self.window.addstr(1 + i, 1, str(text), curses.color_pair(1))
            i += 1
        self.window.refresh()

    def putText(self, text):
        self.textLines[-1] = str(text)
        self.render()

    def shift(self, l, n):
        """This method rotates table elements. i.e. a=[1,2,3] shift(a,1), rotates a to [2,3,1]"""
        return l[n:] + l[:n]

    def shiftText(self):
        self.textLines = self.shift(self.textLines, 1)

    @property
    def getWindowBottomPosition(self):
        return self.pos_y + self.height - 1


class Button(object):
    def __init__(self, key, pos_x, pos_y, offset=0):
        self.WIDTH = 7
        self.HEIGHT = 3
        self.key = key
        self.offset = offset
        self.pos_x = pos_x * self.WIDTH + 1
        self.pos_y = pos_y * self.HEIGHT + 1 + self.offset
        self.text_x = int(self.WIDTH/2)
        self.text_y = int(self.HEIGHT/2)
        self.window = curses.newwin(self.HEIGHT, self.WIDTH, self.pos_y, self.pos_x)
        self.render('default')

    def render(self, color):
        #self.window.clear()
        self.window.border(0)
        if (color == 'red'):
            self.window.addstr(self.text_y, self.text_x, str(self.key), curses.color_pair(1))
        else:
            self.window.addstr(self.text_y, self.text_x, str(self.key))
        self.window.refresh()

    def animate(self):
        self.render('red')
        sleep(0.1)
        self.render('default')

    @property
    def get_key(self):
        return self.key


# This allows the file to be used as a SCRIPT
if __name__ == "__main__":
    init_curses()
    main_window = MainWindow(CALC_WIDTH, CALC_HEIGHT, CALC_TITLE)
    display_window = DisplayWindow(DISP_LINES, DISP_WIDTH, 0, 0)

    keys = []
    keys.append(Button('1', 0, 0, display_window.getWindowBottomPosition))
    keys.append(Button('2', 1, 0, display_window.getWindowBottomPosition))
    keys.append(Button('3', 2, 0, display_window.getWindowBottomPosition))
    keys.append(Button('4', 0, 1, display_window.getWindowBottomPosition))
    keys.append(Button('5', 1, 1, display_window.getWindowBottomPosition))
    keys.append(Button('6', 2, 1, display_window.getWindowBottomPosition))
    keys.append(Button('7', 0, 2, display_window.getWindowBottomPosition))
    keys.append(Button('8', 1, 2, display_window.getWindowBottomPosition))
    keys.append(Button('9', 2, 2, display_window.getWindowBottomPosition))
    keys.append(Button('0', 0, 3, display_window.getWindowBottomPosition))
    keys.append(Button('.', 1, 3, display_window.getWindowBottomPosition))

    keys.append(Button('+', 4, 0, display_window.getWindowBottomPosition))
    keys.append(Button('-', 5, 0, display_window.getWindowBottomPosition))
    keys.append(Button('*', 4, 1, display_window.getWindowBottomPosition))
    keys.append(Button('/', 5, 1, display_window.getWindowBottomPosition))
    keys.append(Button('=', 5, 3, display_window.getWindowBottomPosition))

    text_string = ''
    event = -1
    function_pressed = False
    try:
        while True:
            if event > 0 and event < 255:
                key = filter_char(chr(event), ALLOWED_CHARACTERS)
                function = filter_char(chr(event), ALLOWED_FUNCTIONS)
                if  len(function) == 0:
                    if function_pressed:
                        display_window.shiftText()
                        function_pressed = False
                    text_string += key
                    display_window.putText(text_string)
                else:
                    function_pressed = True
                    text_string = ''
                    display_window.shiftText()
                    display_window.putText(function)

                for key_it in keys:
                    if key_it.get_key == key:
                        key_it.animate();

            main_window.render()
            display_window.render()
            for key_it in keys:
                key_it.render('default')

            event = main_window.getWindow.getch()

            if event == 27:
                """ESC button meaning, Exit app."""
                break
    finally:
        curses.endwin()
