import curses
import time

screen = curses.initscr()
curses.noecho()
screen.keypad(1)
x,y = 0,0
userinput = ord('p')

while userinput != ord('q'):

	screen.clear()
	screen.addstr(y,x,'HelloWorld')
	screen.refresh()
	userinput = screen.getch()
	
	if userinput == curses.KEY_UP:
		y -= 1 
	elif userinput == curses.KEY_DOWN:
		y += 1
	elif userinput == curses.KEY_LEFT:
		x -= 1
	elif userinput == curses.KEY_RIGHT:
		x += 1
curses.endwin()
