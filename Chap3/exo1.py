


#note_int  = input("Quel est votre note_int ? : ")

#Gestion des erreurs
note_int = 0
while note_int == 0:
    note_int  = input("Quel est votre note_int  -? : ")
    try:
        note_int = int(note_int ) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if note_int == 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif note_int < 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            note_int = 0   #je réaffecte 0 à note_int pour revenir à la condition initiale
        elif note_int > 20:
            print("Note incorect !!")
        
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)

            print("Vous avez obtenu {} ".format(note_int))

        if note_int >= 18 :
            
            print("Exellent!")

        if 14<= note_int < 18 :
            
            print("tres bien!")

        if 10<= note_int  < 14:
            
            print("assez bien")

        if 5<= note_int  < 10:
            
            print("insuffisant")

        if note_int  < 5 :
            
            print("Catastrophique")