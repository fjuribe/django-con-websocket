from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from integers.models import *
import requests


# Create your views here.
def index(request):
	return render(request,'index.html',context={'text':'hello world'})



class Prueba(APIView):
	def get(self, request, format=None):
		return HttpResponse(JsonResponse({"success":"holaa"}),content_type="application/json", status=200)

	def post(self, request, format=None):
		full_name=request.data['full_name']
		job=request.data['job']
		email=request.data['email']
		phone=request.data['phone']

		persona=Person.objects.create(
			full_name=full_name,
			job=job,
			email=email,
			phone=phone
		)
		return HttpResponse(JsonResponse({"success":"true"}),content_type="application/json", status=200)


# class Guardar(APIView):