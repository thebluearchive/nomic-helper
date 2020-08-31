

class Parent1(Grandparent):
	def __init__(self):
		self.property1 = "I have this property"

class Parent2(object):
	def __init__(self):
		self.property2 = "I have another property"

class Child(Parent1, Parent2):
	pass


test = Child()
print(test.grandproperty)