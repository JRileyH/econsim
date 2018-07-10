class Actor():
	def __init__(self, name, init):
		self.__name = name
		self.__store = {
			'manpower': init['manpower'],
			'credit': init['credit'],
			'raw': init['raw'],
			'ware': init['ware']
		}

	@property
	def name(self):
		return self.__name

	@property
	def store(self):
		return self.__store

	@property
	def manpower(self):
		return self.__store['manpower']

	@property
	def credit(self):
		return self.__store['credit']

	@property
	def raw(self):
		return self.__store['raw']

	@property
	def ware(self):
		return self.__store['ware']

	def add(self, storeType, amount):
		self.__store[storeType]+=amount
	
	def tick(self):
		print(self.__name+': No tick set')

	def listAssets(self):
		print(self.__name+' Assets: ')
		print('--MANPOWER: '+str(self.manpower))
		print('--CREDIT--: '+str(self.credit))
		print('--RAW-----: '+str(self.raw))
		print('--WARE----: '+str(self.ware))
