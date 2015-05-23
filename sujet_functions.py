#! etc/bin

import os 
import time

##this will be my first function in Python

## for the first functio nlet's think about a function that will show param1 pram2 time

def ma_premier_function (param1, param2):
	i=0
	while i<param2:
		print(i,param1)
		i+=1
	
def ma_seconde_function (param_1,param_2):
	i=0
	result=0
	while i<param_2:
		result=i*param_1
		print(result)
		i+=1
def function_carree(param_1):
	return param_1*param_1

# End function  



#utilisation de la function carree

a=5
print(a)
b=function_carree(a)
print(b)

time.sleep(5)
