#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import math


class Pendulo:
	def __init__(self,massa, l, angulo, angular):
		self.m = massa
		self.l = l
		self.theta = angulo
		self.w = angular
		self.w0 = (g/l)**0.5
		self.T = 2*math.pi*math.sqrt(l/g)
		self.E = 0.5*massa*(l*angular)**2+massa*g*l*(1-math.cos(angulo))
	def a(self,x,v,tt):
		return -self.w0**2*math.sin(x)-gamma*v+A*math.sin(wf*tt)
	def move(self,tt):
		a1 = self.a(self.theta,self.w,tt)
		self.theta += self.w*dt+0.5*a1*dt*dt
		at = self.a(self.theta,self.w,tt)
		vt = self.w+0.5*(a1 + at)*dt
		at = self.a(self.theta,vt,tt)
		self.w += 0.5*(a1 + at)*dt
		p1.theta = (p1.theta+math.pi)%(2*math.pi)-math.pi 
		p2.theta = (p2.theta+math.pi)%(2*math.pi)-math.pi
		self.E = 0.5*self.m*self.w**2+self.m*g*self.l*(1-math.cos(self.theta))
		
A=1.2
dt = 0.01
g = 9.8 
gamma = 0.5
wf = 2./3.
m = 1
l = 10
p1=Pendulo(1.,10.,0.523333333,0)
p2=Pendulo(1.,10.,0.523233333,0)

tt=0
tmax=20*p1.T
t=np.arange(0,tmax,dt)
x=np.zeros(t.size)
x2=np.zeros(t.size)
v=np.zeros(t.size)
v2=np.zeros(t.size)
e=np.zeros(t.size)
dthe=np.zeros(t.size)
dw=np.zeros(t.size)

for i in range(t.size):
		p1.move(t[i])
		p2.move(t[i])
		x[i],x2[i],v[i],v2[i],e[i]=p1.theta,p2.theta,p1.w,p2.w,p1.E
		dthe[i]=(x[i]-x2[i])**2
		dw[i]=(v[i]-v2[i])**2



#n.6

plt.figure(figsize=(8,5),facecolor='white')
plt.axis([0,50,0,200])
plt.xticks(np.linspace(0,10,11,endpoint=True))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)
ax.yaxis.set_label_coords(-0.05,0.5)

plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{$Tempo$}')
plt.ylabel(r'\textit{$Energia$}')
plt.title(r'Pendulo For\c{c}ado - Energia', fontsize=18)

plt.plot(t, e,'g',linewidth=1, label=r'\textit{A=1.2, $\gamma = 0.5, w_f = \frac{2}{3}$}' )
plt.legend(bbox_to_anchor=(1.1, 1), loc=1, borderaxespad=0.001)


plt.savefig("penduloenergy.pdf",dpi=96)

