'''
7. Haz un programa que lea un real x≥0 y que escriba ⌊x⌋ (la parte entera inferior de x), ⌈x⌉ (la parte entera superior de x), y el 
redondeo de x.

Input: 4.8
    
Output: ⌊x⌋: 4, ⌈x⌉: 5, redondeo: 5
'''

x= float (input('Introduzca un número decimal: '))

entero= math.trunc(x)
redondeado= round(x)


print('valor entero: {}, redondeado: {}'.format(entero, redondeado))


#correccion

x = float(input('Introduce un número decimal:'))
x_int = int(x)

if x == x_int:
    print(x)
else:
    parte_inferior = x_int
    parte_superior = x_int + 1
    redondeo = int(x + 0.5)
    print('⌊x⌋: {}, ⌈x⌉: {}, redondeo: {}'.format(parte_inferior, parte_superior, redondeo))


