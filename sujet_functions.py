#! etc/bin



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
# End function  

ma_seconde_function(5,500000)
