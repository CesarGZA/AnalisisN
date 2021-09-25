""" 
Garza Ceja Cesar Eduardo
Facultad de Ingeniería
Analisis numerico 
"""
#Libreria para usar la funcion diff para derivar
from sympy import *
#Usando x,y, z como simbolos y no como variables
x,y,z = symbols('x y z')
fS = diff(x*exp(x)-1,x)
def f(x):
    return x*exp(x)-1

def g(x):
    return fS
def newtonRaphson(x0,e,N):
    print('\n\n--------- Metodo de Newton Rhapson ---------')
    print('Se calculara la raíz de la funcion x*exp(x)-1 \n')
    step = 1 #Iteracon
    flag = 1 #Bandera para acabar el programa deacuerdo al nummax de iteraciones
    condition = True
    while condition:
        if g(x0) == 0.0:#Error division entre cero
            print('Division entre cero, Error!')
            break
        
        x1 = x0 - f(x0)/g(x0).subs(x,x0) #Ecuacion de recurrencia
        #Impreción de datos
        print('Iteracion-%d, x1 = %0.6f y f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1 #Acotamiento de intervalo
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nLa raíz es: %0.8f' % x1)
    else:
        print('\nNo converge')

#Inicia el programa
x0 = float(input('Valor inicial '))
e = float(input('Tolerancia: '))
N = int(input('Iteracion maxima: ')) 

newtonRaphson(x0,e,N)