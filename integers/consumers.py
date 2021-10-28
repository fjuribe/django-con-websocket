from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from integers.models import *
import requests
# from integers.models import *


class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()

		for i in range(1000):
			self.send(json.dumps({'message':randint(1,100)}))
			sleep(1)

	# def disconnect(self, close_code):
	# 	pass
	# def receive(self, text_data):
	# 	pass

class Probando(WebsocketConsumer):
	def connect(self):
		self.accept()

		# longer=self.scope['url_route']
		# print(">>>>",longer)

		personas=Person.objects.get(id=2)
		obj={
			"id":personas.id,
			"persona":personas.full_name
		}
		self.send(json.dumps({'dato':obj}))


class Probando2(WebsocketConsumer):
	def connect(self):
		self.accept()

		longer=self.scope['url_route']['kwargs']
		print(longer)
		id2=longer['id']=5

		try:
			personas=Person.objects.get(id=id2)
			obj={
				"id":personas.id,
				"persona":personas.full_name
			}
			self.send(json.dumps({'dato':obj}))
		except Person.DoesNotExist:
			self.send(json.dumps({'dato':"No existe"}))


