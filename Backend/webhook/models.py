# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class child_model(models.Model):
	id=models.AutoField(default=0,primary_key=True)
	name=models.CharField(maxlength=50)
	age=models.IntegerField()
	total_evaluations=models.IntegerField(default=0)
	score=models.IntegerField(default=100)

class parent_model(models.Model):
	id=models.AutoField(deault=0,primary_key=True)
	name=models.CharField(maxlength=50)
	child_id=models.IntegerField()

#Keyed by evaluation no and child_id
class A_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()
	

class B_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class C_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class D_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class E_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class F_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class G_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class H_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class I_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class J_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class K_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class L_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class M_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class N_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class O_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class P_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class Q_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class R_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class S_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class T_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class U_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class V_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class W_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class X_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class Y_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()

class Z_transactions(models.Model):
	child_id=models.IntegerField()
	evaluation_no=models.IntegerField()
	score=models.IntegerField(default=100)
	total_time=models.FloatField()
	no_of_strokes=models.IntegerField()
	total_length()=models.FLoatField(default=0)
	time_delay=models.FloatField()
	

