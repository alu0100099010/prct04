#!/usr/bin/python
#!encoding: UTF-8

#la diferencia con el ejercicio anterior es que ahora
#la condición del cero está mal, el tercer if debe poner 
#la ecuación tiene infinitas soluciones. 

from math import sqrt
a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))
if a == 0 and b == 0 and c == 0:
  print 'La ecuacion tiene infinitas soluciones'
elif a == 0 and b == 0: #ya sabemos que el c es distuinto de c
  print 'La ecuacion no tiene solucion'
elif a == 0: # cuando b y c son distintos de cero
  x = -c / b
  print 'La solucion de la ecuacion es: x=%4.3f' % x
else: #cuando todos son distintos de cero
      x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
      x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
      print 'Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)