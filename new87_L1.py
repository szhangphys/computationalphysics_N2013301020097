import math
import matplotlib.pyplot as plt 


class Cannon:
	def __init__(self, speed, angle, f = None, pos = None, g = None):
		#time, vel, pos, f, g
		_angle = angle / 180.0 * math.pi
		self.time = 0
		self.vel = [speed * math.cos(_angle), speed * math.sin(_angle)] # float
		if pos != None:  self.pos = list(pos)
		else:  self.pos = [0, 0]
		if f != None: self.f = f ##
		if g != None: self.g = g
		else:  self.g = -9.8

 	# drag acceleration caused by wind
	def f(self, height, speed):	
		_a = 6.5e-3		# K/m
		_alpha = 2.5
		_T_0 = 300.0		# K, sea level temperature
		_B2_m = 4e-5	# /m
		if (1 - _a * height / _T_0) <= 0:	return 0
		return - (1 - _a * height / _T_0)**_alpha * _B2_m * speed**2

 	# return drag [a_x, a_y] # using f()
 	def F_drag(self):
 		_speed = (self.vel[0]**2 + self.vel[1]**2)**0.5
 		_a = self.f( self.pos[1], _speed )
 		_a_x = self.vel[0] / _speed * _a
 		_a_y = self.vel[1] / _speed * _a 
 		return [_a_x, _a_y]

 	# update vel and pos in dt
 	def update(self, dt):
 		self.pos[0] += self.vel[0] * dt
 		self.pos[1] += self.vel[1] * dt
 		_a = self.F_drag()
 		self.vel[0] += _a[0] * dt
 		self.vel[1] += _a[1] * dt + self.g * dt
 		self.time += dt

 	def get_pos(self):
 		return self.pos
 	def get_vel(self):
 		return self.vel
 	def get_time(self):
 		return self.time


#############################################################

def shoot(hyouka):
	t = 200 # s
	n = 10000
	point = 1000
	dt = 1.0 * t / n
	highest = 0
	x_list = []
	y_list = []
	def print_data():
		print "time: ", hyouka.get_time(), "  highest point: ", highest
		print "pos: ", hyouka.get_pos()
		print "vel: ", hyouka.get_vel()
		print "F_drag:", hyouka.F_drag()

	for p in range(point):
		x_list.append(hyouka.get_pos()[0] / 1000.0)
		y_list.append(hyouka.get_pos()[1] / 1000.0)
		for i in range( n/point ):
			hyouka.update(dt)
			if hyouka.get_pos()[1] > highest: highest = hyouka.get_pos()[1] 
			if hyouka.get_pos()[1] <= 0:  
				x_list.append(hyouka.get_pos()[0] / 1000.0) # km
				y_list.append(hyouka.get_pos()[1] / 1000.0) # km
				print_data()
				return [x_list, y_list]


hyouka = Cannon(700, 45)
track1 = shoot(hyouka)

def f(height, speed):	
	_B2_m = 4e-5	# /m
	return -  _B2_m * speed**2

asuka = Cannon(700, 35, f)
track2 = shoot(asuka)

plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('Cannon shell trajectory')
plt.text(13, 7, 'With density correction')
plt.text(12, 4, 'Without density correction')

plt.plot(*track1)
plt.plot(*track2)
plt.show()
