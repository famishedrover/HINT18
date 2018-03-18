# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json ,requests,random,base64,io,datetime,cv2,numpy

from models import *
from letter_funcs import *
from eval_funcs import *
transactions_list=[
	A_transactions,
	B_transactions,
	C_transactions,
	D_transactions,
	E_transactions,
	F_transactions,
	G_transactions,
	H_transactions,
	I_transactions,
	J_transactions,
	K_transactions,
	L_transactions,
	M_transactions,
	N_transactions,
	O_transactions,
	P_transactions,
	Q_transactions,
	R_transactions,
	S_transactions,
	T_transactions,
	U_transactions,
	V_transactions,
	W_transactions,
	X_transactions,
	Y_transactions,
	Z_transactions,
]
letter_funcs_list=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26]
evaulation_funcs_list=[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20,g21,g22,g23,g24,g25,g26]
letter_setter_funcs_list=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26]

clusters_values=[
	{'straight':1,'slant':2,'curved':0},
	{'straight':1,'slant':0,'curved':2},
	{'straight':0,'slant':0,'curved':1},
	{'straight':1,'slant':0,'curved':1},
	{'straight':4,'slant':0,'curved':0},
	{'straight':3,'slant':0,'curved':0},
	{'straight':1,'slant':0,'curved':1},
	{'straight':3,'slant':0,'curved':0},
	{'straight':3,'slant':0,'curved':0},
	{'straight':2,'slant':0,'curved':1},
	{'straight':1,'slant':2,'curved':0},
	{'straight':2,'slant':0,'curved':0},
	{'straight':2,'slant':2,'curved':0},
	{'straight':2,'slant':1,'curved':0},
	{'straight':0,'slant':0,'curved':2},
	{'straight':1,'slant':0,'curved':1},
	{'straight':0,'slant':1,'curved':2},
	{'straight':1,'slant':1,'curved':1},
	{'straight':0,'slant':0,'curved':2},
	{'straight':2,'slant':0,'curved':0},
	{'straight':0,'slant':0,'curved':2},
	{'straight':0,'slant':2,'curved':0},
	{'straight':0,'slant':4,'curved':0},
	{'straight':0,'slant':2,'curved':0},
	{'straight':1,'slant':2,'curved':0},
	{'straight':2,'slant':1,'curved':2},
]



weights ={
	'straight':1,
	'slant':2,
	'curved':3,
}

clusters={
	'straight':[],
	'slant':[],
	'curved':[]
}

def preprocess():
	for i in xrange(26):
		character=chr(i+ord('A'))
		for cluster_type in clusters_values[i].keys():
			clusters[cluster_type].append((character,clusters_values[i][cluster_type]))

def strokes(letter):
	sum=0
	for i in clusters_values[ord(letter)-ord('A')]:
		sum=sum+clusters_values[ord(letter)-ord('A')][i]
	return sum

## curl -H "Content-Type: application/json" -X POST -d '{"id":1,"number":5}' http://localhost:8000/webhook/letter/

error_message=' Incomplete Data Provided '

class LetterView(generic.View):
	# Sends {'symbols':[['A',0],['B',1],['C',3],['D',1],['E',1]]}
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Letter View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
		print "YAHAAN"
		# print repr(self.request.body),type(self.request.body)
		received_dict=json.loads(self.request.body)
		# print received_dict
		if 'id' and 'number' in received_dict:
			child_id=int(received_dict['id'])
			child_id=5 ## this one
			required_number=int(received_dict['number'])
			child_entry=child_model.objects.get(id=child_id)
			candidate_symbols=[]
			for i in xrange(len(letter_funcs_list)):
				curr_letter=chr(i+ord('A'))
				curr_function=letter_funcs_list[i]
				curr_score=curr_function(child_entry)
				curr_eval_func=evaulation_funcs_list[i]
				last_eval=curr_eval_func(child_entry)
				curr_cluster_score=((clusters_values[i]['straight']*weights['straight']+clusters_values[i]['slant']*weights['slant']+clusters_values[i]['curved']*weights['curved'])*100)/18;
				alpha=70
				candidate_symbols.append((curr_score*alpha+curr_cluster_score*(1-alpha),curr_letter,last_eval))
			candidate_symbols=sorted(candidate_symbols,key=lambda x:-x[0])
			for i in xrange(required_number):
				candidate_symbols[i]=[candidate_symbols[i][1],candidate_symbols[i][2]]
			R=HttpResponse(json.dumps({'symbols':candidate_symbols[:required_number]}))
			return R
		else:
			return HttpResponse(error_message)

# Working with ML Model 

from runcheck import actualData
from word import *

class LetterResponse(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Letter Response</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
		preprocess()
		# returns [child_id,eval_no,letter,score(I will calculate ),total_time,no_of_strokes,total_length=0->default,time delay,image]
		received_dict=json.loads(self.request.body)
		if 'Image' and 'child_id' and 'eval_no' and 'letter' and 'score' and 'total_time' and 'no_of_strokes' and 'total_length' and 'time_delay' in received_dict:
			print received_dict['eval_no']
			eval_no=int(float(received_dict['eval_no']))
			print "chalo"
			child_id=int(float(received_dict['child_id']))
			child_id=5 ## this one
			given_letter=received_dict['letter']
			curr_score=float(received_dict['score'])
			total_time=float(received_dict['total_time'])
			no_of_strokes=int(float(received_dict['no_of_strokes']))
			total_length=float(received_dict['total_length'])
			time_delay=float(received_dict['time_delay'])
			writing_time=total_time-time_delay
			avg_time_per_stroke=writing_time/no_of_strokes
			avg_delay_time=time_delay/(no_of_strokes-1+0.0000004)
			img=received_dict['Image']
			img=base64.b64decode(img)
			filenn='canvas'+str(datetime.datetime.now())+".png"
			with open(filenn,'wb') as ff:
				ff.write(img)	
			npimage = cv2.imread(filenn)
			x=npimage.shape[0]
			y=npimage.shape[1]
			npimage = cv2.cvtColor(npimage,cv2.COLOR_BGR2GRAY)
			ml_answer=actualData(npimage,received_dict['letter'])
			# print 'ML ANSWER IS ' ,ml_answer,' given letter ',received_dict['letter']
			given_letter_prob,actual_letter_prob,actual_letter=ml_answer


			
			# ## Updated values for the given letter
			# print transactions_list[ord(given_letter)-ord('A')]
			# print transactions_list[ord(given_letter)-ord('A')].objects
			# print transactions_list[ord(given_letter)-ord('A')].objects.get(child_id=child_id,evaluation_no=eval_no)

			child_entry=child_model.objects.get(id=child_id)
			print 'his name is',child_entry.name

			given_letter_entry=transactions_list[ord(given_letter)-ord('A')](child_id=child_id,evaluation_no=0,score=100,total_time=0,no_of_strokes=1,total_length=1,time_delay=1)
			try:
				given_letter_entry=transactions_list[ord(given_letter)-ord('A')].objects.get(child_id=child_id,evaluation_no=eval_no)
			except:
				pass
			# # print type(given_letter_entry)
			# # print given_letter_entry.child_id,given_letter_entry.evaluation_no
			# # print letter_funcs_list[ord(given_letter)-ord('A')]
			prev_score=letter_funcs_list[ord(given_letter)-ord('A')](child_entry)

			required_no_of_strokes=strokes(given_letter)
			eps=0.00002
			
			curr_score=given_letter_prob*65+(abs(no_of_strokes-required_no_of_strokes)/9.0)*10+(2.71**(-avg_delay_time))*15+(2.71**(-avg_time_per_stroke))*10
			final_score=(curr_score*50+prev_score*50)/(100.0)+eps
			letter_setter_funcs_list[ord(given_letter)-ord('A')](child_entry,final_score)
			# # print transactions_list[ord(given_letter)-ord('A')]
			# # print child_id
			# # print eval_no+1
			# # print final_score
			# # print total_time
			# # print no_of_strokes,total_length,time_delay
			new_transaction=transactions_list[ord(given_letter)-ord('A')](child_id=child_id,evaluation_no=eval_no+1,score=curr_score,total_time=total_time,no_of_strokes=no_of_strokes,total_length=total_length,time_delay=time_delay)

			
			new_transaction.save()
			#  # <------
			
			
			child_entry.score=(child_entry.score*100-prev_score+final_score)/100
			
			child_entry.save() 
			# # <------
			
			# ## Updated values for the actual letter

			prev_score=letter_funcs_list[ord(actual_letter)-ord('A')](child_entry)
			final_score=prev_score-0.25+eps

			letter_setter_funcs_list[ord(actual_letter)-ord('A')](child_entry,final_score)
			 # <------
			# curr_score=update(child_id,no_of_strokes,avg_time_per_stroke,avg_delay_time,given_letter,given_letter_prob,actual_letter,actual_letter_prob)
			return HttpResponse(json.dumps({"Score":curr_score}))
		else:
			return HttpResponse(error_message)


availaible_words=["CAT","BAT","TOY","WOW"]

class WordView(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Word View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):

		received_dict=json.loads(self.request.body)
		print received_dict
		if 'id' and 'number' in received_dict:
			child_id=int(received_dict['id'])
			child_id=5 ## this one
			required_number=int(received_dict['number'])
			child_entry=child_model.objects.get(id=child_id)
			candidate_symbols=[]
			for i in xrange(len(letter_funcs_list)):
				curr_letter=chr(i+ord('A'))
				curr_function=letter_funcs_list[i]
				curr_score=curr_function(child_entry)
				curr_eval_func=evaulation_funcs_list[i]
				last_eval=curr_eval_func(child_entry)
				curr_cluster_score=((clusters_values[i]['straight']*weights['straight']+clusters_values[i]['slant']*weights['slant']+clusters_values[i]['curved']*weights['curved'])*100)/18;
				alpha=70
				candidate_symbols.append((curr_score*alpha+curr_cluster_score*(1-alpha),curr_letter,last_eval))
			candidate_symbols=sorted(candidate_symbols,key=lambda x:x[0])
			print candidate_symbols
			temp_val=[0 for i in xrange(26)]
			for pos in xrange(len(candidate_symbols)):
				i=candidate_symbols[pos]
				temp_val[ord(i[1])-ord('A')]=pos
			
			candidate_words=[]

			for ww in availaible_words:
				
				cost=0
				for ch in ww:
					cost=cost+temp_val[ord(ch)-ord('A')]
				print ww,cost
				candidate_words.append((ww,cost))
			candidate_words=sorted(candidate_words,key=lambda x:x[1])
			print candidate_words
			R=HttpResponse(json.dumps({'words':candidate_words[:required_number]}))
			print R
			return R
		else:
			return HttpResponse(error_message)
		return HttpResponse("<html><b>Post Request to Word View</b></html>")

class WordResp(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Word View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
		received_dict=json.loads(self.request.body)
		print received_dict.keys()
		if 'Image' and 'child_id' and  'word' and 'score' and 'total_time' and 'no_of_strokes' and 'total_length' and 'time_delay' in received_dict:
			child_id=int(float(received_dict['child_id']))
			child_id=5 ## this one
			given_word=received_dict['word']
			curr_score=float(received_dict['score'])
			total_time=float(received_dict['total_time'])
			no_of_strokes=int(float(received_dict['no_of_strokes']))
			total_length=float(received_dict['total_length'])
			time_delay=float(received_dict['time_delay'])
			writing_time=total_time-time_delay
			avg_time_per_stroke=writing_time/no_of_strokes
			avg_delay_time=time_delay/(no_of_strokes-1+0.0000004)
			img=received_dict['Image']
			img=base64.b64decode(img)
			filenn='canvas'+str(datetime.datetime.now())+".png"
			with open(filenn,'wb') as ff:
				ff.write(img)	
			npimage = cv2.imread(filenn)
			x=npimage.shape[0]
			y=npimage.shape[1]
			npimage = cv2.cvtColor(npimage,cv2.COLOR_BGR2GRAY)
		
			ml_answer=segment_word(npimage,given_word)
			for i in xrange(len(ml_answer)):
				given_letter=given_word[i]
				given_letter_prob=ml_answer[i][0]
				actual_letter_prob=ml_answer[i][1]
				actual_letter=ml_answer[i][2]
				child_entry=child_model.objects.get(id=child_id)
				# update(child_id,given_letter,given_letter_prob,actual_letter,actual_letter_prob)

				given_letter_entry=transactions_list[ord(given_letter)-ord('A')](child_id=child_id,evaluation_no=0,score=100,total_time=0,no_of_strokes=1,total_length=1,time_delay=1)
				try:
					given_letter_entry=transactions_list[ord(given_letter)-ord('A')].objects.get(child_id=child_id,evaluation_no=eval_no)
				except:
					pass
				prev_score=letter_funcs_list[ord(given_letter)-ord('A')](child_entry)
				required_no_of_strokes=strokes(given_letter)
				eps=0.00002
				curr_score=given_letter_prob*65+(abs(no_of_strokes-required_no_of_strokes)/9.0)*10+(2.71**(-avg_delay_time))*15+(2.71**(-avg_time_per_stroke))*10
				final_score=(curr_score*50+prev_score*50)/(100.0)+eps
				letter_setter_funcs_list[ord(given_letter)-ord('A')](child_entry,final_score)
				eval_no=evaulation_funcs_list[ord(given_letter)-ord('A')](child_entry)
				new_transaction=transactions_list[ord(given_letter)-ord('A')](child_id=child_id,evaluation_no=eval_no+1,score=curr_score,total_time=total_time,no_of_strokes=no_of_strokes,total_length=total_length,time_delay=time_delay)
				new_transaction.save()
				child_entry.score=(child_entry.score*100-prev_score+final_score)/100
				child_entry.save() 
				prev_score=letter_funcs_list[ord(actual_letter)-ord('A')](child_entry)
				final_score=prev_score-0.25+eps
				letter_setter_funcs_list[ord(actual_letter)-ord('A')](child_entry,final_score)
			return HttpResponse(json.dumps({"Score":curr_score}))
		else:
			return HttpResponse("<html><b>Post Request to Word View</b></html>")

class AnalyticsView(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("<html><b>Get Request to Analytics View</b></html>")
	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)
	def post(self,request,*args,**kwargs):
		received_dict=json.loads(self.request.body)
		id=received_dict['id']
		given_letter=received_dict['letter']
		print id,given_letter
		transactions=transactions_list[ord(given_letter)-ord('A')].objects.filter(child_id=id)
		return HttpResponse("<html><b>Post Request to Analytics View</b></html>")


