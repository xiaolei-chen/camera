"""
Author: Z
Date: 2015-12-3 
"""


import numpy as np 

class node(object):
	def __init__(self):
		self.power = [] 
		self.a = [] 

	def set(self,ar,p):
		for i in xrange(len(ar)):
			self.a.append(ar[i])
			self.power.append(p[i])
	def printf(self):
		print 'a[] is: ',
		for i in xrange(np.array(self.a).shape[0]):
			print self.a[i],
		print ' '
		print 'power[] is: ',
		for i in xrange(np.array(self.power).shape[0]):
			print self.power[i],
		print ' '
############################# base function area #####################
	def parse(self,string):
		"""
		parse str "string" into list "a" and "power"
		"a" means the factor of x 
		"power" means the index of x 
		"""
		self.power = []
		self.a = []
		string = string.replace(' ','')
		eq =  string.find('=')
		new_string = string[(eq+1):]
		index = new_string.find('x')
		while(index != -1):
			if new_string[index-1]=='*' and new_string[index-2].isdigit():
				i = index-2
				num = ""
				while i>=0 and new_string[i].isdigit():
					num = new_string[i] + num
					i = i - 1 
				if i>=0 and new_string[i] == '-':
					num = '-' + num
				self.a.append(float(num))
			else:
				self.a.append(1.)

			if new_string[index+1] == '^':
				num = 0.
				i = index + 2
				while i<len(new_string) and new_string[i].isdigit():
					num = 10*num + float(new_string[i])
					i = i + 1
				self.power.append(num)
			else:
				self.power.append(1.)
			index = new_string.find('x',index+1)
		if new_string[-1] != 'x':
			ll = len(new_string) - 1
			num = ""
			while ll>=0 and new_string[ll].isdigit():
				num = new_string[ll] + num
				ll = ll - 1 
			if ll >= 0 and new_string[ll] == '-':
				num = '-' + num 
			self.a.append(float(num))
			self.power.append(0.)

	def get_fun_value(self,num):
		ret = 0. 
		for i in xrange(np.array(self.a).shape[0]):
			ret += self.a[i] * pow(num,self.power[i])
		return ret 

####################### tool function area ##############

	def Min_push_forward(self,start,step):
		if self.get_fun_value(start) < self.get_fun_value(start + step):
			step_len = -1*step
		x1 = start 
		x2 = start + step 
		y2 = self.get_fun_value(x2) 
		while True:
			x3 = x2 + step 
			y3 = self.get_fun_value(x3) 
			if y2 > y3:
				x1 = x2 
				x2 = x3 
			else:
				break
		return x1,x3 
	def Min_insert_forword(self,lef,rig,max_epochs,min_error):
		epoch = 0
		while True:
			mid1 = (3.*lef - rig)/2. 
			mid2 = (lef + rig)/2.
			y1 = self.get_fun_value(mid1)
			y2 = self.get_fun_value(lef)
			y3 = self.get_fun_value(mid2)
			y4 = self.get_fun_value(rig)
			if y1 <=y2 and y1 <=y3 and y1<=y4:
				lef = mid1 
				rig = lef 
			elif y2<=y1 and y2<=y3 and y2<=y4:
				lef = mid1
				rig = mid2 
			elif y3<=y4 and y3<=y1 and y3<=y2:
				lef = lef 
				rig = rig 
			else:
				lef = mid2
				rig = rig 
			epoch += 1 
			if epoch >= max_epochs or (rig-lef)<=min_error:
				break
		x = (lef + rig)/2.
		y = self.get_fun_value(x)
		return x,y


	def Max_push_forward(self,start,step):
		if self.get_fun_value(start) > self.get_fun_value(start + step):
			step_len = -1*step
		x1 = start 
		x2 = start + step 
		y2 = self.get_fun_value(x2) 
		while True:
			x3 = x2 + step 
			y3 = self.get_fun_value(x3) 
			if y2 < y3:
				x1 = x2 
				x2 = x3 
			else:
				break
		return x1,x3 
	def Max_insert_forword(self,lef,rig,max_epochs,min_error):
		epoch = 0
		while True:
			mid1 = (3.*lef - rig)/2. 
			mid2 = (lef + rig)/2.
			y1 = self.get_fun_value(mid1)
			y2 = self.get_fun_value(lef)
			y3 = self.get_fun_value(mid2)
			y4 = self.get_fun_value(rig)
			if y1>=y2 and y1>=y3 and y1>=y4:
				lef = mid1 
				rig = lef 
			elif y2>=y1 and y2>=y3 and y2>=y4:
				lef = mid1
				rig = mid2 
			elif y3>=y4 and y3>=y1 and y3>=y2:
				lef = lef 
				rig = rig 
			else:
				lef = mid2
				rig = rig 
			epoch += 1 
			if epoch >= max_epochs or (rig-lef)<=min_error:
				break
		x = (lef + rig)/2.
		y = self.get_fun_value(x)
		return x,y


	def min_fun(self,start,step,max_epochs,min_error):
		[lef,rig] = self.Min_push_forward(start,step)
		x,y = self.Min_insert_forword(lef,rig,max_epochs,min_error)
		print 'x: ',x 
		print 'y: ',y 

	def max_fun(self,start,step,max_epochs,min_error):
		[lef,rig] = self.Max_push_forward(start,step)
		x,y = self.Max_insert_forword(lef,rig,max_epochs,min_error)
		print 'x: ',x 
		print 'y: ',y 



if __name__ == '__main__':
	ss = 'f(x) = x^3 - 2*x + 1'
	a = node() 
	a.parse(ss) 
	a.printf()

	max_epochs = 1000 
	min_error = 0.001 
	start = 0.0 
	step = 0.2 
	a.min_fun(start,step,max_epochs,min_error)




