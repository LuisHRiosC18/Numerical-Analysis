from math import *

def f(t,x):
	return eval(s)

def Euler(a,b,n,xa):
	fun= [xa]
	ti= [a]
	h= (b-a)/n
	for i in range(n+1):
		xsig= fun[i] + h*f((ti[i]),(fun[i]))
		fun.append(xsig)
		ti.append(ti[i]+h)
	return [ti,fun]

a= eval(input("Tiempo inicial???= "))
b= eval(input("Tiempo final???= "))
n= eval(input("n??= "))
s= input("Cual es la función???= ")
xa= eval(input("Cual es la condicion inicial??= "))


Eu= Euler(a,b,n,xa)
print("t		|		x(t)")
for i in range(n+1):
	print(f"{Eu[0][i]}			{Eu[1][i]}")

archivo = open('Euler.txt','w')
for a in range(n+1):
	t= Eu[0][a]
	x= Eu[1][a]
	archivo.write(str(t) + '\t' + str(x) + '\n' )
	
archivo.close()
