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


class LetterView(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Letter View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
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


