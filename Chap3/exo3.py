
import random
nb1 = random.randint(1,100)
nb2 = random.randint(1,100)


saisie= 0
while saisie== 0:
    saisie_str = (input(f"Entrer la somme des deux nombre {nb1} et {nb2}: "))

    try:
        saisie_int = int(saisie) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if saisie== 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif saisie< 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            saisie= 0   #je réaffecte 0 à saisiepour revenir à la condition initiale
        elif saisie> 250:
            print("la limite est de 250!")
        
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)

            #print("Vous avez obtenu {} ".format(nb_int))

         if saisie == nb1 + nb2:
            print("Bravo")
         else:
            print("Grrrrrrrrrrrrrrrrr")
    
        

            





