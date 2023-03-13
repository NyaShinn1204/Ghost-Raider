#points to commands that help request info/actions using the gateway
from .guild.request import GuildRequest
from .dms.request import DmRequest
from .user.request import UserRequest
from .media.request import MediaRequest

from ..RESTapiwrap import * #idk man

class Request(object):
	def __init__(self, gatewayobject):
		self.gatewayobject = gatewayobject #remember that the requests session obj is also passed in here

	def setStatus(self, status, activities=[], afk=False, since=0):
		UserRequest(self.gatewayobject).setStatus(status, activities, afk, since)

	def lazyGuild(self, guild_id, channel_ranges, typing=None, threads=None, activities=None, members=None):
		GuildRequest(self.gatewayobject).lazyGuild(guild_id, channel_ranges, typing, threads, activities, members)

	def searchGuildMembers(self, guild_ids, query, limit=10, presences=True):
		GuildRequest(self.gatewayobject).searchGuildMembers(guild_ids, query, limit, presences)

	def DMchannel(self, channel_id):
		DmRequest(self.gatewayobject).DMchannel(channel_id)

	def call(self, channelID, guildID=None, mute=False, deaf=False, video=False):
		MediaRequest(self.gatewayobject).call(channelID, guildID, mute, deaf, video)

	def endCall(self):
		MediaRequest(self.gatewayobject).endCall()