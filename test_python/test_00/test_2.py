class test2:
	def __init__(self, name, mazot):
		self.name = name
		self.mazot = mazot

class test1:
	test3 = []
	def __init__ (self, name):
		self.name = name
		self.tonbelat = []
		test1.test3.append(self)
	

	def add(self, add):
		self.tonbelat.append(add)

	class static:
		@classmethod
		def report(cls):
			res = 0
			for owner in test1.test3:
				for t in owner.tonbelat:
				    res += t.mazot
			return res



owner = test1("owner1")
owne1 = test1("owner2")
owner.add(test2("hamid", 23))
owner.add(test2("hamid", 23))
owne1.add(test2("hamid", 23))
owne1.add(test2("hamid", 23))
owne1.add(test2("hamid", 23))




print(f"total mazot ==> {test1.static.report(owner)}")