#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math

g=9.8
dt=0.01
A=0
gama=0
wf=0
		
p1= pendulo(1,10,np.pi*0.5,0)
tmax=40*p1.T
t=np.arange(0,tmax,dt)
x=np.arange(t.size)
v=np.arange(t.size)
e=np.arange(t.size)
x[0]=p1.theta
v[0]=p1.w
e[0]=p1.E


class Pendulo:
	def __init__(self,massa, l, angulo, angular):
		self.m=massa
		self.l=l
		self.theta=angulo
		self.w=angular
		self.w0=(g/l)**0.5
		self.T=2*np.pi*sqrt(l/g)
	def a(self,x,v,t):
		return -self.w0**2*math.sin(x)-gama*v+A*math.sin(wf*t)
	def move(self,t):
		self.theta=self.theta + self.w*dt+0.5*a(self.theta,self.w,t)*dt*dt
		at=self.a(self.theta,self.w,t)
		vt=self.w+0.5*(self.a + at)*dt
		at=self.a(self.theta,self.wt,t)
		self.w=self.w+0.5*(self.a + at)*dt
		self.a=self.a(self.theta,self.w,t)
		self.E=0.5*self.m*self.w**2-self.m*g*self.l*(1-math.cos(self.theta))
		

		
p1= pendulo(1,10,np.pi*0.5,0)
tmax=40*p1.T
t=np.arange(0,tmax,dt)
x=np.arange(t.size)
v=np.arange(t.size)
e=np.arange(t.size)
x[0]=p1.theta
v[0]=p1.w
e[0]=p1.E


	for i in range(t.size):
		p1.move(t[i])
		x[i],v[i],e[i]=p1.theta,p1.w,p1.E
		
		
		

