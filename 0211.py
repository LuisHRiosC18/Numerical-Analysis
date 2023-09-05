from math import *
def f(t,x):
	return eval(s)
	
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
	
	
a= 0
b= 3
n= 100
xa= 0
s= " 100*(sin(t) - x) "

RK4= RuKu4(n,a,b,xa)

for i in range(n+1):
	print(f"{RK4[0][i]}				{RK4[1][i]} ")
	
	
archivo = open('RK043.txt','w')

for a in range(n+1):
	t= RK4[0][a]
	x= RK4[1][a]
	archivo.write(str(t) + '\t' + str(x) + '\n' )
archivo.write('\n')
archivo.close()

	
