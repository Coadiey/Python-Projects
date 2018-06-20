class HoloceneYear():
	def __init__(self, year):
		self.__year = year
	def setYear(self, year):
		self.__year = year
	def getYear(self):
		return self.__year
	def getGregorianYear(self):
		if self.__year >= 10000: return str(self.__year - 10000) + " AD"
		return str(10000 - self.__year) + " BC"
	def setWithGregorianYear(self, year, ad=True):
		if ad: self.__year = year + 10000
		else: self.__year = 10000 - year
	def isLeapYear(self):
		if self.__year % 4 != 0: return False
		if self.__year % 100 != 0: return True
		if self.__year % 400 != 0: return False
		return True
