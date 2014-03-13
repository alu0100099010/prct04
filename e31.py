#!/usr/bin/python
#!encoding: UTF-8

# coje el numero introducido, lo eleva a potencia y muestra la operación : eleva el numero a 
# la potencia 2, 3, 4, 5. Un ejemplo de el ejecutable:
#2 elevado a 2 es 4
#2 elevado a 3 es 8
#2 elevado a 4 es 16
#2 elevado a 5 es 32


from math import sqrt

numero = int( raw_input('Introduzca un numero '))
for potencia in [2,3,4,5]:
  print '%d elevado a %d es %d' % (numero, potencia, numero**potencia)