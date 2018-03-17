# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json 
import requests
import random
import base64
import io

from models import *
import letter_funcs import *
transactions_map=[(A_transactions,'A'),(B_transactions,'B')]
letter_funcs_map=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26]
## curl -H "Content-Type: application/json" -X POST -d '{"id":1,"number":5}' http://localhost:8000/webhook/letter/

error_message=' Incomplete Data Provided '

class LetterView(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Letter View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
		received_dict=json.loads(self.request.body)
		if 'id' and 'number' in received_dict:
			child_id=received_dict['id']
			required_number=received_dict['number']
			candidate_symbols=[]
			child_entry=child_model.get(id=child_id)

			print child_id,required_number
			return HttpResponse(json.dumps(candidate_symbols))
		else:
			return HttpResponse(error_message)
		return HttpResponse("<html><b>Post Request to Letter View</b></html>")

class WordView(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Word View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Post Request to Word View</b></html>")

class AnalyticsView(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Analytics View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Post Request to Analytics View</b></html>")


