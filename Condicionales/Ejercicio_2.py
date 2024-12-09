'''
2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula, si es una minúscula, si es una vocal, y si es una 
consonante.

Input: 'Z'

Output:
    
Z es consonante
Z es mayuscula

'''



a=input('Introduzca una letra: ')

if a.islower():
    print('{} es minúscula'.format(a))
else:
    print('{} es mayúscula'.format(a))

if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print('{} es una vocal'.format(a))
else:
    print('{} es una consonante'.format(a))
