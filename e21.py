#!/usr/bin/python
#!encoding: UTF-8

a = float(raw_input(’Valor de a: ’))
b = float(raw_input(’Valor de b: ’))
 
# Propuesta:
if (a==0) :
  print "Error, no se puede dividir por cero."
else:
  x = -b/a  
  print ’Solucion: ’, x
