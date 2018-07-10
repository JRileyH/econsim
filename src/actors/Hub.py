from src.actors.Actor import Actor
from src.actors.Generator import Generator
from src.actors.Producer import Producer
from src.actors.Distributor import Distributor
from src.actors.Consumer import Consumer

class Hub(Actor):
	def __init__(self, name):
		Actor.__init__(self,name, {
			'manpower':0,
			'credit':0,
			'raw':0,
			'ware':0
		})
		self.__members = {
			'generator': [
				Generator('gen1', self),
				Generator('gen2', self)
			],
			'producer': [
				Producer('pro1', self),
				Producer('pro2', self)
			],
			'distributor': [
				Distributor('dis1', self),
				Distributor('dis2', self)
			],
			'consumer': [
				Consumer('con1', self),
				Consumer('con2', self)
			]
		}

	@property
	def generators(self):
		return self.__members['generator']
	@property
	def producers(self):
		return self.__members['producer']
	@property
	def distributors(self):
		return self.__members['distributor']
	@property
	def consumers(self):
		return self.__members['consumer']

	def transact(self, take, actor, transactee, amount):
		transactor = None
		for x in self.__members[actor]:
			if x.store[take] > amount:
				if transactor is None:
					transactor = x
				elif x.store[take] > transactor.store[take]:
					transactor = x
		if transactor is not None:
			transactee.add('credit', -amount)
			transactee.add(take, amount)
			transactor.add('credit', amount)
			transactor.add(take, -amount)

	def tick(self):
		for g in self.generators:
			g.tick()
		for p in self.producers:
			p.tick()
		for d in self.distributors:
			d.tick()
		for c in self.consumers:
			c.tick()

	def listAll(self, msg):
		print('*******************************')
		print(self.name+': '+msg)
		print('*******************************')
		for g in self.generators:
			g.listAssets()
		for p in self.producers:
			p.listAssets()
		for d in self.distributors:
			d.listAssets()
		for c in self.consumers:
			c.listAssets()
		self.listAssets()