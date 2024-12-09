'''
3. Haz un programa que lea un entero que representa una temperatura en grados Celsius, y que diga si hace calor, si hace frío, o si se 
está bien. Suponed que hace calor si la temperatura es más alta que 30 grados, que hace frío si es más baja que 10 grados, y que se está 
bien en otro caso.

Input: 25

Output: 'Se está bien'
'''

t= int (input('Introduzca los grados: '))

if t<10:
    subir_temperatura= 23 - t
    calefacción_23grados= t + subir_temperatura
    print('Hace frío. Hay que subir la calefacción {} grados'.format(subir_temperatura))
    print("La calefacción ahora está a {} grados".format(calefacción_23grados))
elif t>30:
    bajar_temperatura= t - 15
    aire_15grados= t - bajar_temperatura
    print('Hace calor. Hay que poner el aire acondicionado para bajar {} grados'.format(bajar_temperatura))
    print("El aire acondicionado ahora está a {} grados".format(aire_15grados))
else:
    print('Se está bien')
