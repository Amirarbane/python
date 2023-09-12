
nb_int = 0
while nb_int == 0:
    nb_int  = input("Quel est votre nombre ? : ")
    try:
        nb_int = int(nb_int ) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if nb_int == 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif nb_int < 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            nb_int = 0   #je réaffecte 0 à nb_int pour revenir à la condition initiale
        elif nb_int > 20:
            print("nb de ligne trop élevé!!")
        
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)

            #print("Vous avez obtenu {} ".format(nb_int))

         for i in range(11):
            resultat = nb_int*i
            print(f"{nb_int}x{i}={resultat}")