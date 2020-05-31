# Python program to explain os.get_terminal_size() method  
    
# importing os module  
import os, sys
from time import sleep
  
# Get the size 
# of the terminal 
columns = os.get_terminal_size().columns
lines = os.get_terminal_size().lines
  


size = columns
for i in range(101):
	bar = size-6
	string = "["
	for j in range(bar):
		if ((i is not 0) and (j < bar * i/100)):
			string += "#"
		else:
			string += " "
	string+= "]" +str(i)+"%"
	sys.stdout.write("\u001b[1000D" + string)
	sys.stdout.flush()
	sleep(.03)

