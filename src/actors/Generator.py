from src.actors.Member import Member 

class Generator(Member):
	def __init__(self, name, hub):
		Member.__init__(self, name, hub, {
			'manpower':0,
			'credit':0,
			'raw':100,
			'ware':0
		})
	
	def tick(self):
		if self.credit > 0:
			self.hub.transact('manpower', 'consumer', self, 1)
		if self.manpower > 0:
			self.add('manpower', -1)
			self.add('raw', 1)