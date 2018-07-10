from src.actors import *

hub = Hub('test')

for i in range(2000):
    hub.listAll(str(i))
    hub.tick()