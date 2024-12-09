'''
1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. Escribe en una línea indicando si a < b, a > b o a = b. 
Ejemplo: a = Anna, b = Javier, Anna < Javier.

Input: 'Anna' 'Javier'
    
output: Anna < Javier
'''

a=input('Introduzca una palabra: ')
b=input('Introduzca otra palabra: ')

if a<b:
    print('{} < {}'.format(a,b))

if a>b:
    print('{} > {}'.format(a,b))

if a==b:
    print('{} = {}'.format(a,b))


