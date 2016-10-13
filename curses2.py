import curses
import time

screen = curses.initscr()

for x in range(10):
	screen.clear()
	screen.addstr(0, x, 'HelloWorld')
	screen.refresh()
	time.sleep(0.1)

curses.endwin()
