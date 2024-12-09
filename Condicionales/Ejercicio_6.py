'''
6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.

Input:

3
5
59

Output: h: 3, m: 6, s: 0
'''

s=int(input('Introduce los segundos: '))
m= int(input('Introduce los minutos: '))
h= int (input('Introduce las horas: '))

if s+1 > 59:
    s=0
    m+=1
    if m>59:
        m=0
        h+=1
else:
    s=+1

print('{}:{}:{}'.format(h,m,s))



