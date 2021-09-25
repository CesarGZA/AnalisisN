from math import exp

""" 
Garza Ceja Cesar Eduardo
Facultad de Ingeniería
Analisis numerico 
"""
def f1(x):
    return x*exp(x)-1

def Biseccion(a,b,e):
    step = 1 #Iteracon
    condition = True
    while condition:    
        x0 = ((a+b)/2)
        print('x0 = %0.6f'%(x0))
        FunE = f1(x0)
        if FunE == 0:
            print('Iteracion %d, a = %0.1f b = %0.1f y f(x0) = %0.6f'% (step, a, b , FunE))
            print('\nEl valor de la raíz es ',x0)
            break
            
        elif FunE < 0 :
            print('Iteracion %d, a = %0.1f b = %0.1f y f(x0) = %0.6f'% (step, a, b , FunE))
            a = x0
            step = step + 1
            
        else:
            print('Iteracion %d, a = %0.1f b = %0.1f y f(x0) = %0.6f'% (step, a, b , FunE))
            step = step + 1
            b = x0
        if step == 16:break
    return

a = float(input('valor a: '))
b = float(input('valor b: '))
e = float(input('tolerancia: '))
Biseccion(a,b,e)