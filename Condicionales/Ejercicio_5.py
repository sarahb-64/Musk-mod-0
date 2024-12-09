'''
5. Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días. Después de la reforma gregoriana, los años 
bisiestos son los múltiplos de cuatro que no acaban en dos ceros, y también los acabados en dos ceros tales que el número que queda 
después de sacar los dos ceros finales es divisible por cuatro. Así, 1800 y 1900, a pesar de ser múltiples de cuatro, no fueran 
bisiestos; en cambio, 2000 lo fue.

Input: 2000

Output: 'Bisiesto'

'''

x= int(input('Introduzca un año: '))

if y==x/100



#correccion
x = int(input('Introduce un año:'))

# Múltiplo de 4
# No termina en dos ceros
# Divisible por 4 omitiendo las dos últimas cifras

if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
    print('Bisiesto')
else:
    print('No bisiesto')
