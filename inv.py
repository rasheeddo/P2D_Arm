import numpy as np
import matplotlib.pyplot as plt

global l2, l3
l2 = 350
l3 = 350

x_cir = np.array([], dtype=float)
z_cir = np.array([], dtype=float)

for i in range(360):
	x = (l2+l3)*np.cos(np.radians(i))
	z = (l2+l3)*np.sin(np.radians(i))

	x_cir = np.append(x_cir, x)
	z_cir = np.append(z_cir, z)


def INV(px,pz):
	global l2, l3

	alpha = np.arctan2(pz,px)
	# print("alpha: ", np.degrees(alpha))
	L = np.sqrt(px**2 + pz**2)
	#from cosine law
	gam = np.arccos(-((L**2 - l2**2 - l3**2)/(2*l2*l3)))
	# print("gam: ", np.degrees(gam))
	#from sine law
	beta = np.arcsin(l3*np.sin(gam)/L)

	theta3 = -(np.pi - gam)
	theta2 = alpha + beta

	# theta2 = np.degrees(theta2)
	# theta3 = np.degrees(theta3)

	return theta2, theta3

def FWD(rad2,rad3):
	global l2, l3

	p2x = l2*np.cos(rad2)
	p2z = l2*np.sin(rad2)
	# print("p2x: ", p2x)
	# print("p2z: ", p2z)

	p3x = l2*np.cos(rad2) + l3*np.cos(rad2+rad3)
	p3z = l2*np.sin(rad2) + l3*np.sin(rad2+rad3)
	# print("p3x: ", p3x)
	# print("p3z: ", p3z)

	return [p2x,p2z] ,[p3x,p3z]



rad2, rad3 = INV(350,350)

print("deg2: ", np.degrees(rad2))
print("deg3: ", np.degrees(rad3))
quit()



### Test plot multiple points

pz_array = np.linspace(-250, 400,  num=25)
px_array = np.linspace(500, 200, num=25)

rad2_array = np.array([])
rad3_array = np.array([])

X = np.array([])
Z = np.array([])

for i in range(len(px_array)):
	rad2, rad3 = INV(px_array[i], pz_array[i])

	[p2x,p2z] , [p3x,p3z] = FWD(rad2,rad3)

	X = np.append(X,[0, p2x, p3x, 0])
	Z = np.append(Z,[0, p2z, p3z, 0])

print(X)
print(Z)
# print(P2)
# print(P3)
plt.plot(x_cir,z_cir, color='r', linewidth=2.0)

for i in range(int(len(X)/4)):
	plt.plot(X[4*i:4*i+3],Z[4*i:4*i+3])
# plt.plot(X[0:3],Z[0:3])
# plt.plot(X[4:7],Z[4:7])
# plt.plot(X[8:11],Z[8:11])
plt.axis([-700, 700, -700, 700], color='r', linewidth=2.0)
plt.grid()
plt.show()
