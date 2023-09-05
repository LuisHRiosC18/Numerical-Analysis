from math import *
def f(t,x,y):
	return eval(s)
def g(t,x,y):
	return eval(p)

def K1(h,t,xa,ya):
	return [f(t,xa,ya),g(t,xa,ya)]
	
def K2(h,t,xa,ya):
	return [ f(t + h/2, xa + h*((K1(h,t,xa,ya)[0])/2), ya + h*((K1(h,t,xa,ya)[1])/2)    )  , g(t + h/2, xa + h*((K1(h,t,xa,ya)[0])/2), ya + h*((K1(h,t,xa,ya)[1])/2) ]

def K3(h,t,xa,ya):
	return [ f(t + h/2, xa + h*((K2(h,t,xa,ya)[0])/2), ya + h*((K2(h,t,xa,ya)[1])/2)    )  , g(t + h/2,xa + h*((K2(h,t,xa,ya)[0])/2), ya + h*((K2(h,t,xa,ya)[1])/2) ]
	
def K4(h,t,xa,ya):
	return [ f(t + h/2, xa + h*((K3(h,t,xa,ya)[0])), ya + h*((K3(h,t,xa,ya)[1]))    )  , g(t + h/2,xa + h*((K3(h,t,xa,ya)[0])), ya + h*((K3(h,t,xa,ya)[1])) ]	


def XRK4(h,t,xa,ya):
	return [xa + (h/6)*(K1(h,t,xa,ya)[0]  +  2*K2(h,t,xa,ya)[0]  +  2*K3(h,t,xa,ya)[0]  + K4(h,t,xa,ya)[0]  ), ya + (h/6)*(K1(h,t,xa,ya)[1]  +  2*K2(h,t,xa,ya)[1]  +  2*K3(h,t,xa,ya)[1]  + K4(h,t,xa,ya)[1]  ]
	
def RuKuSis4(n,a,b,xa,ya):
	h= (b-a)/n
	tv= [a]
	xv= [xa]
	yv= [ya]
	for i in range(n+1):
		xv.append( XRK4(h,tv[i],xv[i],yv[i])[0]      )
		yv.append( XRK4(h,tv[i],xv[i],yv[i])[1]      )
		tv.append(tv[i] + h)
	return [tv,xv,yv]
	
	
	
	
	
	
	
	
a= 0
b= 2
n= 100
xa= 1
ya=0
s= " x-y+ 2*t -t**2 - t**3 "
s= " x+y -4*t**2 + t**3 "


RK4S= RuKuSis4(n,a,b,xa,ya)
for i in range(n+1):
	print(f"{RK4[][i]}				{RK4[1][i]} ")
	
	
archivo = open('RK04.txt','w')

for a in range(n+1):
	x= RK4S[1][a]
	y= RK4S[2][a]
	archivo.write(str(t) + '\t' + str(x) + '\n' )
archivo.write('\n')
archivo.close()





