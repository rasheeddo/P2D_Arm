from Palletizer2DOF import *
import numpy as np
import time

p2d = Palletizer()

p2d.RobotTorqueOn()

p2d.GoHome(2000)
time.sleep(2)

## Example points to go
x = np.array([250,250,250,250,250])
z = np.array([300,150,0,-150,-300])

# x = np.array([250,250])
# z = np.array([300,-300])

## should be around 800 to 3000
finishedTime = 500		# ms

Done = False
AllDone = False
i = 0

while not AllDone:

	# Return True when done moving, otherwise return False
	Done = p2d.GotoPointInTime(x[i],z[i],finishedTime)

	if Done:
		# Increase index only when the robot done movement
		i += 1
		# when done all the points just get out of loop
		if i == len(x):
			AllDone = True




