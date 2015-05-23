#!etc/bin



## hey let's play with some strings

Welcome_Message="Bienvenu dans mon programme"




print(Welcome_Message)


for i in Welcome_Message:
	if i in "AEUIOaeuio":
		print(i)
	else:
		print("*")

