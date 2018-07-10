from src.actors.Actor import Actor 

class Member(Actor):
	def __init__(self, name, hub, init):
		Actor.__init__(self, name, init)
		self.__hub = hub
		for resource in self.store:
			self.__hub.add(resource, self.store[resource])

	@property
	def hub(self):
		return self.__hub

	def add(self, storeType, amount):
		super(Member, self).add(storeType, amount)
		self.hub.add(storeType, amount)
