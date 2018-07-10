from src.actors.Member import Member 

class Producer(Member):
	def __init__(self, name, hub):
		Member.__init__(self, name, hub, {
			'manpower':0,
			'credit':0,
			'raw':0,
			'ware':100
		})
	
	def tick(self):
		if self.credit > 0 and self.raw >= self.manpower:
			self.hub.transact('manpower', 'consumer', self, 1)
		if self.credit > 0:
			self.hub.transact('raw', 'generator', self, 1)
		if self.manpower > 0 and self.raw > 0:
			self.add('manpower', -1)
			self.add('raw', -1)
			self.add('ware', 1)