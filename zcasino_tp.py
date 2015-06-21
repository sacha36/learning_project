#!/usr/bin/python
# -*- encoding:utf-8 -*-

########INIT Variables###############
##Dependencies##
from os import system
from random import randrange
from math import ceil



## module 1 Fonction Random customize
def allez_on_joue(choix_joueur):
	choix_joueur= choix_joueur%10
	resultat=randrange(0,9)
	if ( resultat == choix_joueur):
		return 1
	else:
		return 0

def on_mise_une_somme(lamise,lechoix):
	#on verifie si l'utilisateur a gagné ou pas 
	if (allez_on_joue(lechoix)==1):
		print("vous avez gagné !")
		return lamise
	else:
		print("vous avez tout perdu !" )
		return 0
## module 2 arrondir un nombre

def arrondire(a):
	math.ceil(a)


 ## MAIN

print (" Bienvenue au casino de Lasparis ")
i=5
j=0
'''
while j <50:
	print(randrange(4,9))
	j+=1
'''

print(" Zcasino is starting ")
## Variable départ 
cagnotte=1000
print(" Vous venez de vous installer a la table avec ", cagnotte, " $.")
on_continue_de_jouer=1
while on_continue_de_jouer:
	while cagnotte>0:
		#cagnotte=str(cagnotte)
		#print(" il vous reste "+cagnotte)
		cagnotte=on_mise_une_somme(50,9)+cagnotte -50
		cagnotte=int(cagnotte)
		print(cagnotte)	
	print(" Fin de la partie")
	on_continue_de_jouer=0
print ("Finish la soirée est finie ")
