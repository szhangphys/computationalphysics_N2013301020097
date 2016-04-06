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


def reach(hyouka):
	t = 100 # s
	n = 10000 #####
	point = 100
	dt = 1.0 * t / n
	highest = 0
	for p in range(point):
		for i in range( n/point ):
			hyouka.update(dt)
			if hyouka.get_pos()[1] > highest: highest = hyouka.get_pos()[1] 
			if hyouka.get_pos()[1] <= 0:  
				return hyouka.get_pos()
	return -1


def hit_y(v, angle, dist):
	hyouka = Cannon(v, angle)
	t = 1000 # s
	n = 520 ##### 2000 # 100s
	point = 1
	dt = 1.0 * t / n
	highest = 0
	for p in range(point):
		for i in range( n/point ):
			hyouka.update(dt)
			if hyouka.get_pos()[0] > dist:
				return hyouka.get_pos()[1] / 1000.0 # km
			if hyouka.get_pos()[1] < -36000: return None
	return None

DIST = 20000 # m
#for i in range(1500):
#	print hit_y(1500 + i, 30 + i / 100.0, DIST)
v_list = []
y_list = []

for _v in range(110):
	v = 200 + 10 * _v
	for _a in range(179):
		angle = -89 + _a 
		v_list.append(v) 
		y_list.append( hit_y(v, angle, DIST)  )

plt.plot(y_list, v_list, 'm.')
plt.xlabel('target altitude (km)')
plt.ylabel('speed (m/s)')
plt.title('Minimum speed')
#plt.text(13, 7, 'With density correction')
#plt.text(12, 4, 'Without density correction')
plt.show()
