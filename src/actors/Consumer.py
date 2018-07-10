from src.actors.Member import Member 

class Consumer(Member):
	def __init__(self, name, hub):
		Member.__init__(self, name, hub, {
			'manpower':100,
			'credit':0,
			'raw':0,
			'ware':0
		})

	def tick(self):
		if self.credit > 0:
			self.hub.transact('ware', 'distributor', self, 1)
		if self.ware > 0:
			self.add('ware', -1)
			self.add('manpower', 1)