# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class child_model(models.Model):
	id=models.AutoField(default=0,primary_key=True)
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	total_evaluations=models.IntegerField(default=0)
	score=models.IntegerField(default=100)

class parent_model(models.Model):
	id=models.AutoField(default=0,primary_key=True)
	name=models.CharField(max_length=50)
	child_id=models.IntegerField()
	A=models.IntegerField()
	B=models.IntegerField()
	C=models.IntegerField()
	D=models.IntegerField()
	E=models.IntegerField()
	F=models.IntegerField()
	G=models.IntegerField()
	H=models.IntegerField()
	I=models.IntegerField()
	J=models.IntegerField()
	K=models.IntegerField()
	L=models.IntegerField()
	M=models.IntegerField()
	N=models.IntegerField()
	O=models.IntegerField()
	P=models.IntegerField()
	Q=models.IntegerField()
	R=models.IntegerField()
	S=models.IntegerField()
	T=models.IntegerField()
	U=models.IntegerField()
	V=models.IntegerField()
	W=models.IntegerField()
	X=models.IntegerField()
	Y=models.IntegerField()
	Z=models.IntegerField()

# class A_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class B_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class C_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class D_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class E_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class F_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class G_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class H_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class I_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class J_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class K_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class L_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class M_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class N_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class O_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class P_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class Q_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class R_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class S_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class T_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class U_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class V_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class W_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class X_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class Y_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

# class Z_values(models.Model):
# 	child_id=models.IntegerField()
# 	score=models.IntegerField()

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
	
