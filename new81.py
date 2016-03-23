# y = y(x)
# y' = ~y ~x
import matplotlib.pyplot as plt 
import math

def f(deriv, init = (0, 0), x1 = 10, y_range = None, step = 1, point = 1000):
	#return a list of points and derivative value
	#if y get out of range even in the process of computing, stop and return 
	if y_range == None:
		y_range = (-1000 * abs(x1 - init[0]), 1000 * abs(x1 - init[0]))
	x, y = init
	dot = [[x, y, deriv(*init)]]
	dx = 1.0 * (x1 - x) / step / point
	for p in range(point):
		for i in range(step):
			#y += dx * deriv(x, y)
			y += 0.5 * dx *(deriv(x, y) + deriv(x + dx, y + dx * deriv(x, y)))
			x += dx
			if y > y_range[1] or y < y_range[0]: return dot
		dot.append([x, y, deriv(x, y)])
	return dot

def draw_1(deriv, x_range = (-3, 3), y_range = (-3, 3), density = 8, step = 1, point = 1000):
	# real y_range should be much bigger (perhaps 5 times, or 2?)
	# set (avg_x, y in y_realrange) as initial points
	times = 2
	delta_y = y_range[1] - y_range[0]
	avg_y = (y_range[1] + y_range[0]) / 2.0
	y_realrange = (avg_y - delta_y * times / 2.0, avg_y + delta_y * times / 2.0)
	x1 = x_range[1]
	for i in range(times * density + 1):
		init = ((x_range[0] + x_range[1]) / 2.0, (y_realrange[1] - y_realrange[0]) * i / (1.0 * times * density) + y_realrange[0])
		dot_left  = f(deriv, init, x_range[0], y_realrange, step, point/2)
		dot_right = f(deriv, init, x_range[1], y_realrange, step, point/2)
		dot_left.reverse()
		#plot dots and avoid broken lines
		dot_tmp = []
		dotadded = False
		for item in dot_left + dot_right:
			if item[1] <= y_range[1] and item[1] > y_range[0]:
				if not dotadded:
					dotadded = True
				dot_tmp.append(item)
			elif dotadded:
				plt.plot(*trans(dot_tmp))
				dot_tmp = []
				dotadded = False
				continue
		plt.plot(*trans(dot_tmp))

def draw_2(deriv, x_range = (-3, 3), y_range = (-3, 3), density = 8, step = 1, point = 1000):
	delta_y = y_range[1] - y_range[0]
	avg_y  = (y_range[1] + y_range[0]) / 2.0
	delta_x = x_range[1] - x_range[0]
	avg_x  = (x_range[1] + x_range[0]) / 2.0
	for i in range(density + 1):
		dot1_x, dot1_y, dot2_x, dot2_y, dot3_x, dot3_y = [], [], [], [], [], []
		init1 = (x_range[0], delta_y * i / (1.0 * density) + y_range[0])
		init2 = (delta_x * i / (1.0 * density) + x_range[0], y_range[0])
		init3 = (delta_x * i / (1.0 * density) + x_range[0], y_range[1])
		dot_1 = f(deriv, init1, x_range[1], y_range, step, point)
		dot_2 = f(deriv, init2, x_range[1], y_range, step, point)
		dot_3 = f(deriv, init3, x_range[1], y_range, step, point)
		#plot dots, needn't avoid broken lines
		plt.plot(*trans(dot_1))
		plt.plot(*trans(dot_2))
		plt.plot(*trans(dot_3))

def trans(dot):
	dot_x, dot_y = [], []
	for item in dot:
		dot_x.append(item[0])
		dot_y.append(item[1])
	return (dot_x, dot_y)

'''
def deriv(x, y):
	# defferential equation y' = blabla
	return -0.5 * y + x - 0.1*y**2 
	#return math.log(y**2 + 1) * (math.cos(x) + 1)
	#return -x * y
	#return math.e**(-x**2)
draw_1(deriv, (-3, 5), (-30, 20), 12, 1, 1000)
draw_2(deriv, (-3, 5), (-30, 20), 32, 1, 1000)
'''
def f0(x, y):
	return -0.5 * y + x - 0.1*y**2 
def f1(x, y):
	return math.log(abs(y) + 0.000000001) #abs(y)**0.5 # math.e**(-x**2)

'''
draw_1(f0, (-3, 5), (-30, 50), 7)
draw_2(f0, (-3, 5), (-30, 50), 20)
plt.savefig('f0.png')
plt.show()
''''''
draw_1(f1, (-2, 2), (0, 2), 10)
draw_2(f1, (-2, 2), (0, 2), 10)
plt.savefig('f1.png')
plt.show()
 ''''''
plt.plot(*trans(f(f0, (-4, 10), 10)))
plt.savefig('f0+.png')
plt.show()
'''


def deriv(t, v):
	return 10 - v
print f(deriv, (0, 0), 2)[-1]
draw_2(deriv, (-8, 8), (-5, 10))
plt.savefig('deriv+.png')
plt.show()
