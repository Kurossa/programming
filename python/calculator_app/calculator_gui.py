#!/usr/bin/python3
import sys
import curses
from curses.textpad import Textbox, rectangle
from time import sleep

WIDTH = 80
HEIGHT = 50
TIMEOUT = 100
ALLOWED_CHARACTERS = '0123456789+-*/='

def filter_char(char):
    for c in ALLOWED_CHARACTERS:
        if c == char:
            return c
    return ''



def print_function(args_num=0):
    print('Hello World! with',args_num,'arg(s).')

    for i in range(args_num):
        print(sys.argv[i],'\n')
def init_curses():
    curses.initscr()
    curses.beep()
    curses.beep()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.noecho()
    curses.curs_set(0)

def test(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5, 30, 2, 1)
    rectangle(stdscr, 1, 0, 1 + 5 + 1, 1 + 30 + 1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()


class Button(object):
    def __init__(self, key, window, pos_x, pos_y):
        self.WIDTH = 4
        self.HEIGHT = 3
        self.key = key
        self.window = window
        self.pos_x = pos_x * self.WIDTH
        self.pos_y = pos_y * self.HEIGHT

    def render(self):
        #rectangle(self.window, self.pos_y, self.pos_x, self.pos_y + self.HEIGHT, self.pos_x + self.WIDTH)
        self.window.addstr(self.pos_x+1, self.pos_y+1, self.key)
        self.window.refresh()

    def animate(self):
        self.window.refersh()

    #@property
    #def get_key(self):
    #    return self.key



# This allows the file to be used as a SCRIPT
if __name__ == "__main__":
    init_curses()
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    window.border(0)

    key_1 = Button(window, '1', 0, 0)
    #key_2 = Button(window, '2', 0, 1)

    #key_1.render()
    #key_2.render()

    #test(window)
    event_stored = 1

    # Filtering characters in string
    test_str = 'sdfoi2349ujwer-2034=+23d*dsfs/'
    result_str = ''
    for c in test_str:
        result_str += filter_char(c)


    try:

        while True:
            window.clear()
            window.border(0)
            window.addstr(0, 5, 'Calculator v0.1', curses.color_pair(1))
            window.addstr(1, 1, 'Result:'+result_str)

            if event_stored > 0 and event_stored < 255:
                key = filter_char(chr(event_stored))
                #print(key)
                window.addstr(3, 1, key, curses.color_pair(1))
            window.addstr(4, 1, str(event_stored))

            event = window.getch()
            if event > 0:
                event_stored = event

            if event == 27:
                """ESC button meaning, Exit app."""
                break
    finally:
        #print_function(len(sys.argv))
        # #sleep(3)
        curses.endwin()
