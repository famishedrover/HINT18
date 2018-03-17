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
from letter_funcs import *
from eval_funcs import *
transactions_list=[A_transactions,B_transactions,'B']
letter_funcs_list=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26]
evaulation_funcs_list=[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20,g21,g22,g23,g24,g25,g26]
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
			child_entry=child_model.objects.get(id=child_id)
			candidate_symbols=[]
			for i in xrange(len(letter_funcs_list)):
				curr_letter=chr(i+ord('A'))
				curr_function=letter_funcs_list[i]
				curr_score=curr_function(child_entry)
				curr_eval_func=evaulation_funcs_list[i]
				last_eval=curr_eval_func(child_entry)
				candidate_symbols.append((curr_score,curr_letter,last_eval))
			candidate_symbols=sorted(candidate_symbols,key=lambda x:-x[0])
			for i in xrange(required_number):
				candidate_symbols[i]=[candidate_symbols[i][1],candidate_symbols[i][2]]
			print child_id,required_number
			return HttpResponse(json.dumps({'symbols':candidate_symbols[:required_number]}))
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


