#!/usr/bin/python3
import sys
import curses
from curses.textpad import Textbox, rectangle
import calculator_engine
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

class MainWindow(object):
    def __init__(self, width, height, title):
        self.width = width
        self.height = height

class Button(object):
    def __init__(self, key, pos_x, pos_y):
        self.WIDTH = 7
        self.HEIGHT = 3
        self.key = key
        #self.window = window
        self.pos_x = pos_x * self.WIDTH
        self.pos_y = pos_y * self.HEIGHT
        self.text_x = int(self.WIDTH/2)
        self.text_y = int(self.HEIGHT/2)
        self.window = curses.newwin(self.HEIGHT, self.WIDTH, self.pos_y, self.pos_x)
        self.render('default')

    def render(self, color):
        self.window.clear()
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
    window.refresh()

    key_1 = Button('1', 3, 3)
    key_2 = Button('2', 3, 4)

    key_1.animate()
    key_2.animate()

    #sleep(3)
    #test(window)
    event_stored = 1

    # Filtering characters in string
    test_str = 'sdfoi2349ujwer-2034=+23d*dsfs/'
    result_str = ''
    for c in test_str:
        result_str += filter_char(c)


    try:
        #sleep(1)
        while True:
             window.clear()
             window.border(0)
             window.addstr(0, 5, 'Calculator v0.1', curses.color_pair(1))
             window.addstr(1, 1, 'Result:'+result_str)
             #window.addstr(5,1, 'Result from engine: '+calculator_engine.insert_char('d') )

             if event_stored > 0 and event_stored < 255:
                 key = filter_char(chr(event_stored))
                 if key == '1':
                     key_1.animate()
                 elif key == '2':
                     key_2.animate()
                 #print(key)
                 window.addstr(3, 1, key, curses.color_pair(1))
             window.addstr(4, 1, str(event_stored))
             window.refresh()
             key_1.render('default')
             key_2.render('default')

             #sleep(3)
             #break
             event = window.getch()
             if event > 0:
                 event_stored = event
        #
             if event == 27:
                 """ESC button meaning, Exit app."""
                 break
    finally:
        #print_function(len(sys.argv))
        # #sleep(3)
        curses.endwin()
