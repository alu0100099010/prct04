#!/usr/bin/python
#!encoding: UTF-8

#la diferencia con el ejercicio anterior es que ahora
#la condición del cero está mal, el tercer if debe poner 
#la ecuación tiene infinitas soluciones. 

from math import *

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))
if a == 0:
  if b == 0:
    if c == 0:
      print 'La ecuacion no tiene solucion'
    else:
      print 'La ecuacion tiene infinitas soluciones'
  else:
    x = -c / b
    print 'La solucion de la ecuacion es: x=%4.3f' % x
else:
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
  print 'Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)