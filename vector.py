from misc import Failure

class Vector(object):
    
    def __init__(self, arg):
    	if isinstance(arg, (int, long)):
    		if arg < 0:
    			raise ValueError('A vector can not have a negative length.')
    		else:
    			self.list = [0.0 for x in range(arg)]
    	elif isinstance(arg, (tuple, list)):
    		self.list = [x for x in arg]
    	else:
    		raise TypeError('A vector must be instanciated with a length or sequence.')

    def __repr__(self):
    	return 'Vector(' + str(self.list) + ')'

    def __iter__(self):
    	return self.list.__iter__()

    def __len__(self):
    	return len(self.list)

    def __add__(self, other):
    	if isinstance(other, (list, tuple)):
    		return self + Vector(other)
    	else:
    		tmp = []
    		for i, o in enumerate(other):
				#print 'i: ' + str(i) + ' o: ' + str(o)
				tmp.append(self.list[i] + o)
    		return Vector(tmp)

    def __radd__(self, other):
    	return self.__add__(other)

    def dot(self, other):
    	a = self.list
    	b = other if isinstance(other, (tuple, list)) else other.list

    	product = 0
    	for i in range(len(a)):
    		product += a[i] * b[i]
    	return product  

    def __getitem__(self, key):
    	if isinstance(key, int) and key >= len(self.list):
    		raise IndexError('Index of vector out of bounds.')
    	elif isinstance(key, slice):
    		return self.list[key.start:key.stop:key.step]
    	else:
    		return self.list[key]

    def __setitem__(self, key, value):
    	if isinstance(key, slice):
    		self.list[key.start:key.stop:key.step] = value
    	else:
    		self.list[key] = value

  	def hello(self, other):
  		print 'Hello'

  	def __eq__(self, other):
  		for i, s in enumerate(self.list):
  			if s != other[i]:
  				return false
  		return true