# -*- coding: utf-8 -*-
class Person(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.age = 25
		self.add = 'tainguyen20097@gmail.com'
person1 = Person("Tai")
print(person1.add)