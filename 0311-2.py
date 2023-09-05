from math import *
#def f(t,x):
#	return eval(s)

def f(t,x):
	if  t == 0 and x==0:
		return 0
	else:
		return eval(s)

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
b= 1
n= 128
xa= 0
s= " x/t + t*(1/(cos(x/t))) "

RK4= Rugputas(a,b,n,xa)
	
#for i in range(n+1):
#	print(f"{RK4[0][i]}				{RK4[1][i]} ")
	
	


archivo = open('RK04A2.txt','w')

for a in range(n+1):
	t= RK4[0][a]
	x= RK4[1][a]
	archivo.write(str(t) + '\t' + str(x) + '\n' )
archivo.write('\n')
archivo.close()
