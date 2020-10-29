from Palletizer2DOF import *
import numpy as np
import time
import pygame

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

p2d = Palletizer()

p2d.RobotTorqueOn()

p2d.GoHome(2000)
time.sleep(2)

x_neutral = 350
z_neutral = 0

x_add_on = 280
z_add_on = 500

finished_time = 1500

## for continous input like joystick
## the servo needs to be fast, otherwise it will jump between points
p2d.SetTimeBaseProfile(2,300,150)
p2d.SetTimeBaseProfile(3,300,150)

try:
	while True:
		pygame.event.pump()
		axis1 = joystick.get_axis(1)
		axis0 = joystick.get_axis(0)
		axis1 = round(axis1,2)
		axis0 = round(axis0,2)
		# print("axis1: %f  axis0: %f " %(axis1,axis0))

		x_target = -axis0*x_add_on + x_neutral
		z_target = -axis1*z_add_on + z_neutral

		# print("x: %f  z: %f" %(x_target,z_target))
		p2d.GotoByJoystick(x_target, z_target)


except(KeyboardInterrupt, SystemExit):
	pygame.quit()

