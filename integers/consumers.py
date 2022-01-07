from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from integers.models import Person
import requests
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
# from integers.models import *
from channels.generic.websocket import JsonWebsocketConsumer
import channels.layers
from asgiref.sync import async_to_sync
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from asgiref.sync import sync_to_async,async_to_sync

class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		for i in range(9):
			self.send(json.dumps({'message':randint(1,100)}))
			sleep(1)

	def receive(self, text_data):
		pass

	def disconnect(self, close_code):
		pass


class Probando(WebsocketConsumer):
	def connect(self):
		self.accept()
		print("se activo el socket")
		async_to_sync(self.channel_layer.group_add)('timer_observers',self.channel_name)
		self.send({
            "type": "websocket.accept",
        })


	def send_message(self, message):
		print("enviado!",message)
		# await self.send_current_timer()
		self.send({
			"type": "websocket.send",
			"text": "exito"
		})

	def receive(self, text_data):
		pass

	def disconnect(self, close_code):
		pass


######################### PROBADO #################################
class WSConsumerAsync(AsyncConsumer):
	async def websocket_connect(self,event):
		print("Connected!",event)
		await self.channel_layer.group_add("group_name", self.channel_name)

		await self.send({
			"type": "websocket.accept"
		})
	async def websocket_receive(self, event):

		print("Receive!", event)

	async def websocket_disconnect(self, event):
		print("Disconnected!", event)


	async def send_message(self,message):
		print("enviado!",message)
		# index=self.scope['url_route']['kwargs']['id']

		# try:
		# 	personas=Person.objects.get(id=index)
		# 	obj={
		# 		"id":personas.id,
		# 		"persona":personas.full_name,
		# 		"id2":index
		# 	}
		# 	await self.send(json.dumps({'dato':obj}))
		# except Person.DoesNotExist:
		# 	await self.send(json.dumps({'dato':"No existe"}))
		await self.send({
			"type": "websocket.send",
			"text": json.dumps({'dato':message})
		})



#######################################3

class RespuestaModelo(WebsocketConsumer):
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
		id2=longer['id']

		try:
			personas=Person.objects.get(id=id2)
			obj={
				"id":personas.id,
				"persona":personas.full_name,
				"id2":longer['id2']
			}
			self.send(json.dumps({'dato':obj}))
		except Person.DoesNotExist:
			self.send(json.dumps({'dato':"No existe"}))


