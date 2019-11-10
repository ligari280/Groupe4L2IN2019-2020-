@@ -0,0 +1,41 @@
# codage: utf-8
à partir de l' heure d' importation sommeil

def  versement_argent ():
		message =  " Versement argent "
		print (message.upper ())

		print ( " \ n \ n ****************************** \ n " )

		print ( " Versement sur quel compte: ?? " )
		print ( " 1- Courant " )
		print ( " 2- salaire " )
		# print ("3- client")
		# print ("2- étranger")

		reponse =  int ( input ( " >>   " ))
		si réponse ==  1 :
			print ( " Versement sur un compte courant. " )

			somme_a_verser =  int ( input ( " entrer la somme à verser. Somme minimale = 500 fcfa:   " ))
			si somme_a_verser <=  500 :
				print ( " la somme doit être inférieure à 500 fcfa " )
				somme_a_verser =  int ( input ( " entrer la somme à verser. Somme minimale = 500 fcfa:   " ))
				print ( " La somme verser dans votre compte courant est de {} fcfa " .format (somme_a_verser))

			sinon :
				dormir ( 2 )
				nouveau_solde = somme_a_verser
				print ( " La somme versée sur votre compte courant est de {} fcfa " .format (nouveau_solde))

		# ## ++++++++++ compte salarial ++++++++++++ ###

		réponse elif ==  2 :
			print ( " Versement dans votre compte (salaire) " )
			somme_a_verser =  int ( input ( " Entrer la somme:   " ))
			dormir ( 2 )
			print ( " la somme verser dans votre compte est {}  " .format (somme_a_verser))
		sinon :
			print ( " Erreur de choix !! " )

versement_argent ()
