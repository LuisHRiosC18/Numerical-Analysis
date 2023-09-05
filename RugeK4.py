from math import *
def f(t,x):
	return eval(s)
def g(t,y):
	return eval(p)

def K1(h,t,xa):
	return h*f(t,xa)
	
def K2(h,t,xa):
	return h*f(t + h/2, xa + ((K1(h,t,xa))/2)    )

def K3(h,t,xa):
	return h*f(t + h/2, xa + ((K2(h,t,xa))/2)    )
	
def K4(h,t,xa):
	return h*f(t+h , xa + K3(h,t,xa) )
	
def XRK4(h,t,xa):
	return xa + (1/6)*(K1(h,t,xa)  +  2*K2(h,t,xa)  +  2*K3(h,t,xa) + K4(h,t,xa)     )
	
def RuKu4(n,a,b,xa):
	h= (b-a)/n
	tv= [a]
	xv= [xa]
	for i in range(n+1):
		xv.append( XRK4(h,tv[i],xv[i])      )
		tv.append(tv[i] + h)
	return [tv,xv]
	
	
def K11(a,xa,h):
	return h*f(a,xa)
def K12(a,xa,h):
	return h*f(a+h, xa + K11(a,xa,h)) 
def equisb(a,xa,h):
	return xa + (1/2)*(K11(a,xa,h)+K12(a,xa,h)) 
def Rugputas(a,b,n,xa):
	h= (b-a)/n
	tv= [a]
	xv= [xa]
	for i in range(n+1):
		tv.append(a+(i+1)*h)
		xv.append(equisb(tv[i],xv[i],h))
	return [tv,xv]	
	
	
	
	
	
	
	
	
a= 0
b= 1.6
n= 50
xa= 1
s= "  x*sqrt(x**2 -1) "

RK4= RuKu4(n,a,b,xa)
RK2= Rugputas(a,b,n,xa)
RK= [RK2,RK4]
for i in range(n+1):
	print(f"{RK4[0][i]}				{RK4[1][i]} ")
	
	
archivo = open('RK04.txt','w')
for i in range(2):
	for a in range(n+1):
		t= RK[i][0][a]
		x= RK[i][1][a]
		archivo.write(str(t) + '\t' + str(x) + '\n' )
	archivo.write('\n')
archivo.close()





