from src.actors.Member import Member 

class Distributor(Member):
	def __init__(self, name, hub):
		Member.__init__(self, name, hub, {
			'manpower':0,
			'credit':100,
			'raw':0,
			'ware':0
		})

	def tick(self):
		if self.credit > 0:
			self.hub.transact('manpower', 'consumer', self, 1)
		if self.credit > 0 and self.manpower > 0:
			self.add('manpower', -1)
			self.hub.transact('ware', 'producer', self, 1)
			