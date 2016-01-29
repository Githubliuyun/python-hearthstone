class Packet:
	pass


class Action(Packet):
	def __init__(self, ts, entity, type, index, target):
		self.ts = ts
		self.entity = entity
		self.type = type
		self.index = index
		self.target = target
		self.ended = False
		self.packets = []

	def __iter__(self):
		for packet in self.packets:
			yield packet

	def __repr__(self):
		return "%s(entity=%r, type=%r, index=%r, target=%r)" % (
			self.__class__.__name__, self.entity, self.type, self.index, self.target
		)

	def end(self):
		self.ended = True


class ActionMetaData(Packet):
	def __init__(self, ts, type, entity, count):
		self.ts = ts
		self.type = type
		self.entity = entity
		self.count = count
		self.info = []

	def __repr__(self):
		return "%s(type=%r, entity=%r)" % (self.__class__.__name__, self.type, self.entity)


class CreateGame(Packet):
	class Player:
		def __init__(self, ts, entity, playerid, hi, lo):
			self.ts = ts
			self.entity = entity
			self.playerid = playerid
			self.hi = hi
			self.lo = lo
			self.name = ""
			self.tags = []

	def __init__(self, ts, entity):
		self.ts = ts
		self.entity = entity
		self.tags = []
		self.players = []


class HideEntity(Packet):
	def __init__(self, ts, entity, zone):
		self.ts = ts
		self.entity = entity
		self.zone = zone


class FullEntity(Packet):
	def __init__(self, ts, entity, cardid):
		self.ts = ts
		self.entity = entity
		self.cardid = cardid
		self.tags = []


class ShowEntity(Packet):
	def __init__(self, ts, entity, cardid):
		self.ts = ts
		self.entity = entity
		self.cardid = cardid
		self.tags = []


class TagChange(Packet):
	def __init__(self, ts, entity, tag, value):
		self.ts = ts
		self.entity = entity
		self.tag = tag
		self.value = value


class Choices(Packet):
	def __init__(self, ts, entity, id, tasklist, type, min, max):
		self.ts = ts
		self.entity = entity
		self.id = id
		self.tasklist = tasklist
		self.type = type
		self.min = min
		self.max = max
		self.source = None
		self.choices = []

	@property
	def player(self):
		return self.entity


class SendChoices(Packet):
	def __init__(self, ts, id, type):
		self.ts = ts
		self.entity = None
		self.id = id
		self.type = type
		self.choices = []


class ChosenEntities(Packet):
	def __init__(self, ts, entity, id):
		self.ts = ts
		self.entity = entity
		self.id = id
		self.choices = []


class Options(Packet):
	def __init__(self, ts, id):
		self.ts = ts
		self.entity = None
		self.id = id
		self.options = []


class Option(Packet):
	def __init__(self, ts, entity, id, type, optype):
		self.ts = ts
		self.entity = entity
		self.id = id
		self.type = type
		self.optype = optype
		self.options = []


class SendOption(Packet):
	def __init__(self, ts, option, suboption, target, position):
		self.ts = ts
		self.entity = None
		self.option = option
		self.suboption = suboption
		self.target = target
		self.position = position