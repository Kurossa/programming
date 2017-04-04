#!/usr/bin/python3
import sys
import curses
from curses.textpad import Textbox, rectangle
import calculator_engine
from time import sleep

COLOR_REDONWHITE = 1
COLOR_CYANONBLUE = 2
COLOR_BLUEONCYAN = 3
COLOR_WHITEONBLUE = 4
COLOR_WHITEONRED = 5
COLOR_REDONBLUE = 6
COLOR_WHITEONGREEN = 7

CALC_TITLE = 'Calculator v0.8'
DISP_LINES = 4
DISP_WIDTH = 42
CALC_HEIGHT = DISP_LINES + 16
CALC_WIDTH = DISP_WIDTH + 2
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
    curses.init_pair(COLOR_REDONWHITE, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(COLOR_CYANONBLUE, curses.COLOR_CYAN, curses.COLOR_BLUE)
    curses.init_pair(COLOR_BLUEONCYAN, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(COLOR_WHITEONBLUE, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(COLOR_WHITEONRED, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(COLOR_REDONBLUE, curses.COLOR_RED, curses.COLOR_BLUE)
    curses.init_pair(COLOR_WHITEONGREEN, curses.COLOR_WHITE, curses.COLOR_GREEN)
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
        self.window.bkgd(curses.color_pair(COLOR_CYANONBLUE))
        self.window.border(0)
        self.window.addstr(0, 2, self.title, curses.color_pair(COLOR_BLUEONCYAN))
        self.window.refresh()

    def getch(self):
        return self.window.getch()

class HelpWindow(object):
    def __init__(self):
        self.WIDTH = CALC_WIDTH
        self.HEIGHT = CALC_HEIGHT
        self.TITLE = 'Help'
        self.TEXT = 'Calculator written by LGlab & Kurossa\n\n' \
                    '  Used technologies:\n' \
                    '  - Python3\n' \
                    '  - Curses module for GUI\n\n' \
                    '  Key shortcuts:\n' \
                    '    h - displays help window\n' \
                    '    ESC or c - Clears display\n' \
                    '               or Exits help window\n' \
                    '    q - Quits program'
        self.is_show = False
        self.window = curses.newwin(self.HEIGHT, self.WIDTH, 0, 0)

    def show(self):
        self.is_show = True

    def hide(self):
        self.is_show = False

    @property
    def isShow(self):
        return self.is_show

    def render(self):
        if(self.is_show):
            self.window.clear()
            self.window.bkgd(curses.color_pair(COLOR_WHITEONRED))
            self.window.addstr(2, 2, self.TEXT, curses.color_pair(COLOR_WHITEONRED))
            self.window.border(0)
            self.window.addstr(0, 2, self.TITLE, curses.color_pair(COLOR_WHITEONRED))
            self.window.refresh()



class DisplayWindow(object):
    def __init__(self, line_number, width, offset_x, offset_y):
        self.TITLE = 'Result'
        self.WIDTH = width
        self.height = line_number + 2
        self.pos_x = offset_x + 1
        self.pos_y = offset_y + 1
        self.lines = line_number
        self.textLines = ['' for x in range(self.lines)]
        self.window = curses.newwin(self.height, self.WIDTH, self.pos_y, self.pos_x)
        self.render()

    def clear(self):
        self.window.clear()
        self.textLines = ['' for x in range(self.lines)]
        self.render()

    def render(self):
        self.window.clear()
        #self.window.attrset(curses.A_BOLD)
        self.window.bkgd(curses.color_pair(COLOR_WHITEONBLUE)|curses.A_BOLD)
        self.window.border(0)
        self.window.addstr(0, 1, self.TITLE, curses.color_pair(COLOR_WHITEONBLUE)|curses.A_BOLD)
        i = 0
        for text in self.textLines:
            self.window.addstr(1 + i, self.WIDTH - len(text) - 1, str(text), curses.color_pair(COLOR_WHITEONBLUE)|curses.A_BOLD)
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
        #self.render()

    def render(self, attr):
        #self.window.clear()
        self.window.border(0)
        self.window.bkgd(attr)
        self.window.addstr(self.text_y, self.text_x, str(self.key), attr)
        self.window.refresh()

    def animate(self):
        self.render(curses.color_pair(COLOR_WHITEONGREEN)|curses.A_BOLD)
        sleep(0.1)
        self.render(curses.color_pair(COLOR_WHITEONBLUE)|curses.A_NORMAL)

    @property
    def get_key(self):
        return self.key


# This allows the file to be used as a SCRIPT
if __name__ == "__main__":
    init_curses()
    main_window = MainWindow(CALC_WIDTH, CALC_HEIGHT, CALC_TITLE)
    display_window = DisplayWindow(DISP_LINES, DISP_WIDTH, 0, 0)
    help_window = HelpWindow()

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
                key_it.render(curses.color_pair(COLOR_WHITEONBLUE))

            help_window.render()
            event = main_window.getch()

            if event > 0 and event < 255 and chr(event) == 'h':
                """h button meaning, Show help Window."""
                help_window.show()
            elif event > 0 and event < 255 and ( chr(event) == 'c' or event == 27):
                if help_window.isShow:
                    help_window.hide()
                else:
                    """ESC or c button meaning, Clear display. If help Window shown, close it."""
                    text_string = ''
                    display_window.clear()
            elif event > 0 and event < 255 and chr(event) == 'q':
                """q button meaning, Exit app."""
                break
    finally:
        curses.endwin()
