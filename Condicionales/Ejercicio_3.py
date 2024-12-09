'''
3. Haz un programa que lea un entero que representa una temperatura en grados Celsius, y que diga si hace calor, si hace frío, o si se 
está bien. Suponed que hace calor si la temperatura es más alta que 30 grados, que hace frío si es más baja que 10 grados, y que se está 
bien en otro caso.

Input: 25

Output: 'Se está bien'
'''

t= int (input('Introduzca los grados: '))

if t<10:
    print('Hace frío.')
elif t>30:
    print('Hace calor.')
else:
    print('Se está bien')

