# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.



class child_model(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	age=models.FloatField()
	total_evaluations=models.FloatField(default=0)
	score=models.FloatField(default=100)
	evaluationA=models.FloatField(default=0)
	evaluationB=models.FloatField(default=0)
	evaluationC=models.FloatField(default=0)
	evaluationD=models.FloatField(default=0)
	evaluationE=models.FloatField(default=0)
	evaluationF=models.FloatField(default=0)
	evaluationG=models.FloatField(default=0)
	evaluationH=models.FloatField(default=0)
	evaluationI=models.FloatField(default=0)
	evaluationJ=models.FloatField(default=0)
	evaluationK=models.FloatField(default=0)
	evaluationL=models.FloatField(default=0)
	evaluationM=models.FloatField(default=0)
	evaluationN=models.FloatField(default=0)
	evaluationO=models.FloatField(default=0)
	evaluationP=models.FloatField(default=0)
	evaluationQ=models.FloatField(default=0)
	evaluationR=models.FloatField(default=0)
	evaluationS=models.FloatField(default=0)
	evaluationT=models.FloatField(default=0)
	evaluationU=models.FloatField(default=0)
	evaluationV=models.FloatField(default=0)
	evaluationW=models.FloatField(default=0)
	evaluationX=models.FloatField(default=0)
	evaluationY=models.FloatField(default=0)
	evaluationZ=models.FloatField(default=0)
	A=models.FloatField(default=100)
	B=models.FloatField(default=100)
	C=models.FloatField(default=100)
	D=models.FloatField(default=100)
	E=models.FloatField(default=100)
	F=models.FloatField(default=100)
	G=models.FloatField(default=100)
	H=models.FloatField(default=100)
	I=models.FloatField(default=100)
	J=models.FloatField(default=100)
	K=models.FloatField(default=100)
	L=models.FloatField(default=100)
	M=models.FloatField(default=100)
	N=models.FloatField(default=100)
	O=models.FloatField(default=100)
	P=models.FloatField(default=100)
	Q=models.FloatField(default=100)
	R=models.FloatField(default=100)
	S=models.FloatField(default=100)
	T=models.FloatField(default=100)
	U=models.FloatField(default=100)
	V=models.FloatField(default=100)
	W=models.FloatField(default=100)
	X=models.FloatField(default=100)
	Y=models.FloatField(default=100)
	Z=models.FloatField(default=100)

class parent_model(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	child_id=models.FloatField()
	
#Keyed by evaluation no and child_id
class A_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()
	

class B_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class C_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class D_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class E_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class F_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class G_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class H_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class I_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class J_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class K_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class L_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class M_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class N_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class O_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class P_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class Q_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class R_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class S_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class T_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class U_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class V_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class W_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class X_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class Y_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class Z_transactions(models.Model):
	child_id=models.FloatField()
	evaluation_no=models.FloatField()
	score=models.FloatField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.FloatField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()
	
