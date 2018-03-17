# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class child_model(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	total_evaluations=models.IntegerField(default=0)
	score=models.IntegerField(default=100)
	evaluationA=models.IntegerField(default=0)
	evaluationB=models.IntegerField(default=0)
	evaluationC=models.IntegerField(default=0)
	evaluationD=models.IntegerField(default=0)
	evaluationE=models.IntegerField(default=0)
	evaluationF=models.IntegerField(default=0)
	evaluationG=models.IntegerField(default=0)
	evaluationH=models.IntegerField(default=0)
	evaluationI=models.IntegerField(default=0)
	evaluationJ=models.IntegerField(default=0)
	evaluationK=models.IntegerField(default=0)
	evaluationL=models.IntegerField(default=0)
	evaluationM=models.IntegerField(default=0)
	evaluationN=models.IntegerField(default=0)
	evaluationO=models.IntegerField(default=0)
	evaluationP=models.IntegerField(default=0)
	evaluationQ=models.IntegerField(default=0)
	evaluationR=models.IntegerField(default=0)
	evaluationS=models.IntegerField(default=0)
	evaluationT=models.IntegerField(default=0)
	evaluationU=models.IntegerField(default=0)
	evaluationV=models.IntegerField(default=0)
	evaluationW=models.IntegerField(default=0)
	evaluationX=models.IntegerField(default=0)
	evaluationY=models.IntegerField(default=0)
	evaluationZ=models.IntegerField(default=0)
	A=models.IntegerField(default=100)
	B=models.IntegerField(default=100)
	C=models.IntegerField(default=100)
	D=models.IntegerField(default=100)
	E=models.IntegerField(default=100)
	F=models.IntegerField(default=100)
	G=models.IntegerField(default=100)
	H=models.IntegerField(default=100)
	I=models.IntegerField(default=100)
	J=models.IntegerField(default=100)
	K=models.IntegerField(default=100)
	L=models.IntegerField(default=100)
	M=models.IntegerField(default=100)
	N=models.IntegerField(default=100)
	O=models.IntegerField(default=100)
	P=models.IntegerField(default=100)
	Q=models.IntegerField(default=100)
	R=models.IntegerField(default=100)
	S=models.IntegerField(default=100)
	T=models.IntegerField(default=100)
	U=models.IntegerField(default=100)
	V=models.IntegerField(default=100)
	W=models.IntegerField(default=100)
	X=models.IntegerField(default=100)
	Y=models.IntegerField(default=100)
	Z=models.IntegerField(default=100)

class parent_model(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	child_id=models.IntegerField()
	
#Keyed by evaluation no and child_id
class A_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()
	

class B_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class C_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class D_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class E_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class F_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class G_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class H_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class I_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class J_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class K_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class L_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class M_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class N_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class O_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class P_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class Q_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class R_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class S_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class T_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class U_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class V_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class W_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class X_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class Y_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()

class Z_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length=models.FloatField(default=0)
	time_delay=models.FloatField()
	
