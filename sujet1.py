#!etc/bin 


#le but du programme est d'aficher si une année est buisextile ou pas 
#pour se faire :
#si une année n est pas un multiple de 4 s'arrete la elle n est pas bissextile 
#si elle est un multiple de 4 alors :
#	si elle est multiple de 100 
#		si c'est le cas on regarde si multiple de 400
#			si elle est multiple de 400 ok
#			sinon elle l'est pas 
#		sinon  elle l'est ( multiple de 100) 
#		
#

print("Debut du programme")

Annee=0
while (Annee <50000000):

	


	if Annee%4==0:
		if Annee%100==0:
			if Annee%400==0:
				print(Annee)
	


	Annee=Annee+1	 		
