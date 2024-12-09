'''
4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la intersección o indique que esta es vacía.

Input:

20 30

10 20

Output: [20, 20]
'''

x1 = int(input('Introduce el extermo izquierdo del primer intervalo:'))
y1 = int(input('Introduce el derecho izquierdo del primer intervalo:'))

x2 = int(input('Introduce el extermo izquierdo del segundo intervalo:'))
y2 = int(input('Introduce el extermo derecho del segundo intervalo:'))

minimo = x1
if x2 > x1:
    minimo = x2
    
maximo = y1
if y2 < y1:
    maximo = y2
    
if minimo <= maximo:
    print('[{}, {}]'.format(minimo, maximo))
else:
    print('[]')