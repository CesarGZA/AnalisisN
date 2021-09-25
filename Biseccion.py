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
        err = abs(0.567115-x0)
        FunE = f1(x0)
        if err < e:
            print('Iteracion %d, a = %0.1f b = %0.1f x0 = %0.4f y Error = %0.4f'% (step,a,b,x0,err))
            print('\nEl valor de la raíz es %0.4f'%(x0))
            break
            
        elif FunE < 0 :
            print('Iteracion %d, a = %0.1f b = %0.1f x0 = %0.4f y Error = %0.4f'% (step,a,b,x0,err))
            a = x0
            step = step + 1
            
        else:
            print('Iteracion %d, a = %0.1f b = %0.1f x0 = %0.4f y Error = %0.4f'% (step,a,b,x0,err))
            step = step + 1
            b = x0
    return

a = float(input('valor a: '))
b = float(input('valor b: '))
e = float(input('tolerancia: '))
Biseccion(a,b,e)