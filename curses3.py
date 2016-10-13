import curses
import time

screen = curses.initscr()
curses.noecho()
x,y = 0,0

userinput = ord('p')
while userinput != ord('q'):

	screen.clear()
	screen.addstr(y,x,'HelloWorld')
	screen.refresh()
	userinput = screen.getch()
	
	if userinput == ord('w'):
		y -= 1 
	elif userinput == ord('s'):
		y += 1
	elif userinput == ord('a'):
		x -= 1
	elif userinput == ord('d'):
		x += 1
curses.endwin()
