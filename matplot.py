#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math


infile=open('dados.txt','r')
the=[0]
w=[0]
a=[0]
e=[0]
t=[0]
de=[0]


for line in infile:
	x,v,z,b = line.split()
	the.append(float(x))
	w.append(float(v))
	e.append(float(z))
	t.append(float(b))


relax=0
xp,vp,tp = the[relax:],w[relax:],t[relax:]

#graf1
plt.figure(figsize=(8,5),facecolor='white')
plt.axis([0,120,-5,5])
plt.xticks(np.linspace(0,10,11,endpoint=True))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)
ax.yaxis.set_label_coords(-0.025,0.5)

plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{Tempo $(s)$}')
plt.ylabel(r'\textit{The $(Rad)$}')
plt.title(r'Pendulo For\c{c}ado - The$\times$t', fontsize=18)

plt.plot(t,the,'b',linewidth=0.7, label=r'\textit{$\gamma = 0.5, W_0 = 0, W_f = 2/3, A = 1.2 $}') 
plt.legend(bbox_to_anchor=(1.1, 1), loc=1, borderaxespad=0.001)
plt.savefig("pendulothext.pdf",dpi=96)


# graf 2
plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,120,-5,5])
plt.xticks(np.linspace(0,10,11,endpoint=True))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)
ax.yaxis.set_label_coords(-0.025, 0.5)


plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{Tempo $(s)$}')
plt.ylabel(r'\textit{W $(\frac{rad}{s})$}')
plt.title(r'Pendulo For\c{c}ado - W$\times$t', fontsize=18)


plt.plot(t,w,'g',linewidth=0.7, label=r'\textit{$\gamma = 0.5, W_0 = 0, W_f = 2/3, A = 1.2$}')  
plt.legend(bbox_to_anchor=(1.1, 1), loc=1, borderaxespad=0.)
plt.savefig("pendulowxt.pdf",dpi=96)

# graf 3
plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,120,-250,50])
plt.xticks(np.linspace(0,10,11,endpoint=True))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)
ax.yaxis.set_label_coords(-0.07, 0.5)


plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{Tempo $(s)$}')
plt.ylabel(r'\textit{$E$}')
plt.title(r'Pendulo For\c{c}ado - Energy', fontsize=18)


plt.plot(tp,e,'g',linewidth=0.7, label=r'\textit{$\gamma = 0.5, W_0 = 0, W_f = 2/3, A = 1.2 $}')  
plt.legend(bbox_to_anchor=(1.1, 1), loc=1, borderaxespad=0.)
plt.savefig("penduloeenergy.pdf",dpi=96)


infile.close()
  
