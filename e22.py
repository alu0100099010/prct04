#!/usr/bin/python
#!encoding: UTF-8

#

a = float(raw_input(’Valor de a: ’))
b = float(raw_input(’Valor de b: ’))
if a != 0:
  x = -b/a
  print ’Solucion: ’, x
 if a == 0:  #debemos poner ==
  print ’La ecuaci ́on no tiene solución.’