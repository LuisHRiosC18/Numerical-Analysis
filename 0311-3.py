from math import *
def f(t,x):
	if  t == 0 and x==0:
		return 0
	else:
		return eval(s)
	
def K1(h,t,xa):
	return h*f(t,xa)
	
def K2(h,t,xa):
	return h*f(t + h/2, xa + ((K1(h,t,xa))/2)    )

def K3(h,t,xa):
	return h*f(t + h/2, xa +  ((K1(h,t,xa))/4) + ((K2(h,t,xa))/4)    )
	
def K4(h,t,xa):
	return h*f(t+h , xa - ((K2(h,t,xa))) + 2*K3(h,t,xa) )
def K5(h,t,xa):
	return h*f(t+ (2/3)*h , xa + ( (7/27)*(K1(h,t,xa)) + (10/27)*(K2(h,t,xa))) + (1/27)*K4(h,t,xa) )
def K6(h,t,xa):
	return h*f(t + (h/5) , xa + ( (28/625)*(K1(h,t,xa)) - (1/5)*(K2(h,t,xa))) + (546/625)*K3(h,t,xa) + (54/625)*K4(h,t,xa) - (378/625)*K5(h,t,xa) )	



def XRK5(h,t,xa):
	return xa + (    (1/24)*K1(h,t,xa)  +  (5/48)*K4(h,t,xa) +  (27/56)*K5(h,t,xa) +  (125/336)*K6(h,t,xa)     )
	
def RuKu5(n,a,b,xa):
	h= (b-a)/n
	tv= [a]
	xv= [xa]
	for i in range(n+1):
		xv.append( XRK5(h,tv[i],xv[i])      )
		tv.append(tv[i] + h)
	return [tv,xv]


a= 0
b= 1
n= 128
xa= 0
s= " x/t + t*(1/(cos(x/t))) "

RK5= RuKu5(n,a,b,xa)
	
#for i in range(n+1):
#	print(f"{RK5[0][i]}				{RK5[1][i]} ")
	
	


archivo = open('RK05.txt','w')

for a in range(n+1):
	t= RK5[0][a]
	x= RK5[1][a]
	archivo.write(str(t) + '\t' + str(x) + '\n' )
archivo.write('\n')
archivo.close()

