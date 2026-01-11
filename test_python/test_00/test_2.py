class tonobil:
	def __init__(self, 	name, mazot):
		self.name = name
		self.mazot = mazot


class company:
	def __init__(self, name):
		self.name = name
		self.tonoblat = []
	def add_tonobl(self, tonoble):
		self.tonoblat.append(tonoble)
	
	def report(self):
			# total = sum(self.tonoblat)
			count = len(self.tonoblat)
			return f"Company {self.name}: , count={count}"
	class static:

		@staticmethod
		def report(company):
			# total = sum(self.tonoblat)
			count = len(self.tonoblat)
			return f"Company {self.name}: , count={count}"

def main():
	owner = company("owner1")
	test = static()
	tn1  = tonobil("sanr", 23)
	tn2  = tonobil("sanr", 23)
	owner.add_tonobl(tn1)
	owner.add_tonobl(tn2)
	print(owner.report())

if __name__ == "__main__":
	main()


