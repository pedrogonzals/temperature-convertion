'''
Created on Oct 10, 2014

@author: PedroG
'''

print " to this program converts fahrenheit to celsius"
print " type in a temperature in fahrenheit:",
fahrenheit = float(raw_input())
celsius =(fahrenheit - 32)*5.0 /9
print "that is",
print ("%.2f" % celsius),
print " degrees celsius"