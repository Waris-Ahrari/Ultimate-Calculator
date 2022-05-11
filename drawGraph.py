import scipy as sp
import numpy as np
import math
import matplotlib.pylab as plt
import re


def draw(xs, xe, xst, y1, x_axis, y_axis, xy_axes):
	y = 0
	# if "pi" in xs:
	xs = re.sub("pi", "np.pi", xs)
	# if "pi" in xe:
	xe = re.sub("pi", "np.pi", xe)	
	# if "pi" in xst:
	xst = re.sub("pi", "np.pi", xst)	

	# if "sin(" in y1:
	y1 = re.sub("sin\(", "np.sin(", y1)
	# if "sinh" in y1:
	y1 = re.sub("sinh", "np.sinh", y1)	

	# if "cos(" in y1:
	y1 = re.sub("cos\(", "np.cos(", y1)
	# if "cosh" in y1:
	y1 = re.sub("cosh", "np.cosh", y1)
	
	# if "tanh" in y1:
	y1 = re.sub("tanh", "np.tanh", y1)
	# if "tan(" in y1:
	y1 = re.sub("tan\(", "np.tan(", y1)		
			

	# if "log(" in y1:
	y1 = re.sub("log\(", "np.log(", y1)
	
	# if "e" in y1:
	y1 = re.sub("e", "np.e", y1)

	y1 = re.sub("pi", "np.pi", y1)


	y1 = re.sub("sqrt", "np.sqrt", y1)

	y1 = y1.replace("^", "**")

	xs, xe, xst = eval(xs), eval(xe), eval(xst)
	x = np.arange(xs, xe, xst)
	y = eval(y1)

	ax = plt.subplot(1, 1, 1)
	ax.plot(x, y)

	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')

	# if xy_axes == 1:
	# 	ax.spines['left'].set_position('center')
	# 	ax.spines['bottom'].set_position('center')

	# # Hide the right and top spines
	# ax.spines['right'].set_visible(False)
	# ax.spines['top'].set_visible(False)

	# # Only show ticks on the left and bottom spines
	# ax.yaxis.set_ticks_position('left')
	# ax.xaxis.set_ticks_position('bottom')

	plt.show()
	
	
	
	# plt.plot(x,y)
	# plt.show()
