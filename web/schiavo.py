import requests
from urllib.parse import urlencode
from common.discord.webhook import Webhook

class schiavo:
	"""
	Schiavo Bot class
	"""
	def __init__(self, botURL=None, prefix="", maxRetries=20):
		"""
		Initialize a new schiavo bot instance

		:param botURL: schiavo api url.
		:param prefix: text to prepend in every message, can be empty.
		:param maxRetries: max retries if api request fail. 0 = don't retry.
		"""
		self.botURL = botURL
		self.maxRetries = maxRetries
		self.prefix = prefix

	def sendMessage(self, message, botURL):
		"""
		Send a generic message through schiavo api
		:param channel: api channel.
		:param message: message content.
		:param customParams: Let all hell break loose
		:return:
		Let's call it 50% spaghetti code.. Deal..?
		"""

		if botURL is None:
			return
		else:
			embed = Webhook(botURL, color=randint(100000, 999999))
			#embed.set_author(name='Aika', icon='https://a.akatsuki.pw/999', url="http://akatsuki.pw/")
			#embed.set_image('https://i.namir.in//bTr.png')
			#embed.set_title(title="Aika")
			embed.add_field(name=message, value='** **')

		for _ in range(0, self.maxRetries):
			try:
				embed.post()
				break
			except requests.RequestException:
				continue
				
	def sendConfidential(self, message, noPrefix=False):
		"""
		Send a message to #bunk

		:param message: message content.
		:param noPrefix: if True, don't prepend prefix to message.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['confidential']
		self.sendMessage(message, botURL)

	def sendStaff(self, message, noPrefix=False):
		"""
		Send a message to #staff

		:param message: message content.
		:param noPrefix: if True, don't prepend prefix to message.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['staff']
		self.sendMessage(message, botURL)

	def sendGeneral(self, message, noPrefix=True):
		"""
		Send a message to #general

		:param message: message content.
		:param noPrefix: if True, don't prepend prefix to message.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['general']
		self.sendMessage(message, botURL)

	def sendChatlog(self, message, noPrefix=True):
		"""
		Send a message to #chatlog.

		:param message: message content.
		:param noPrefix: if True, don't prepend prefix to message.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['chatlog']
		self.sendMessage(message, botURL)

	def sendCM(self, message, noPrefix=False):
		"""
		Send a message to #communitymanagers

		:param message: message content.
		:param noPrefix: if True, don't prepend prefix to message.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['cm']
		self.sendMessage(message, botURL)
