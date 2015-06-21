#!/usr/bin/python

#programm to use les boucles 
from os import system 
import hashlib
	 

def fonction_calcule_perimetre(a,b):
	peri=a*b
	peri=str(peri)
	print ("le perimetre est "+peri)
def fonction_magique(charset):
	print(hashlib.sha224(charset).hexdigest())

 

'''
print(" hello bidule")
print(" hello machin")
print(" hello encore")
'''
Chaine ='1 2 3 4 5 6 7 8 9 1 0 11 12'
i=0
while i<25:
	i=str(i)
	#print (" "+i+"-> Hello ")
	i=int(i)
	i+=1

print ("#"*75)
j=1
k=1
l=1
while j<256:	
	while k<256:
		while l<256:
			fi=256*256*j+256*k+l
			fi=str(fi)
			fonction_magique(fi)
			fi=int(fi)
			l+=1
		k+=1
		l=0
	k=0	
	j+=1

print ("BYE")

