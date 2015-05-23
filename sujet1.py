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
Annee=2000
print("l'année qu\'on va vérifier est : ",Annee)


if Annee%4==0:
	if Annee%100==0:
		if Annee%400==0:
			print("L'annee ",Annee," est bisex")
		else:
			print("L'annee ",Annee," n\'est pas bisex")
	else:
		print(Annee," n est pas bisex")
else:
	print("l'annnee",Annee,"  nest pas multiple de 4 on s arrette la car elle neest pas bisex ")

	 		
