
import os # j ai importé cette bibliotheque pour pouvoir rafeaichir le terminal apres chaque choix
          # cela rend le programe plus prpore est mieux a utiliser est comprendre
          

def effacer_terminal(): #Voici la fonction qui permet de rafraichir le terminal apres chaque choix d entree , plat et dessert
    os.system('cls' if os.name == 'nt' else 'clear')



print("********Bienvenue au restaurant PyFood**********")



print("les entrees")
print("1- Salade de chef \t 12 €")
print("2- Salade niçoise \t 10 €")
print("3- Salade grecque \t 9 €")
print("4- Salade italienne \t 11 €")


choix_entree = 0

while choix_entree == 0:
    choix_entree_str= input("\n Choisiser votre entrée :   ")
    try :

        choix_entree= int(choix_entree_str)
    except:
        print("Entre des chiffres !")
    else:
        if choix_entree == 0:
            print("Vous avez entrer la valeur 0 pouver vous recommencer ?")
        elif choix_entree > 4:
            print("Aucun choix correspondant")
            choix_entree = 0
        elif choix_entree < 0:
            print("Veuiller entrer une valeur positif !")
            choix_entree = 0
            
        else:
            effacer_terminal()

            if choix_entree == 1 : 
                print("\n Vous avez choisi: la Salade de chef.  ")
                prix_entree=12

            elif choix_entree == 2:
                print("\n Vous avez choisi: la Salade niçoise.  ")
                prix_entree=10

            elif choix_entree == 3:
                print("\n Vous avez choisi: la  Salade grecque . ")
                prix_entree=9

            elif choix_entree == 4:
                print("\n Vous avez choisi: la Salade italienne.  ")
                prix_entree=11
                



print("\n les plats")
print("1- friture de poisson \t 25 €")
print("2- Bavette de veau    \t 19 €")
print("3- Saumon a la plancha\t 22 €")
print("4- Boeuf bourguignon  \t  16 €")


choix_plat = 0

while choix_plat == 0:
    choix_plat_str = input("\n Choisissez votre plat :   ")
    try:
        choix_plat = int(choix_plat_str)
    except:
        print("Veuiller entrer des chiffre !")
    else:
        if choix_plat == 0:
            print("vous avez entrer la valeur 0 pouvez vous recommencer ?")
        elif choix_plat > 4:
            print("Aucun choix correspondant")
            choix_plat = 0
        elif choix_plat < 0:
            print("Le chiffre choisi est négatif !!")
            choix_plat = 0
        else:
            effacer_terminal()

            if choix_plat== 1 : 
                print("\n Vous avez choisi: la friture de poisson . ")
                prix_plat=25

            elif choix_plat == 2:
                print("\n Vous avez choisi: la Bavette de veau . ")
                prix_plat=19

            elif choix_plat == 3:
                print("\n Vous avez choisi: la  Saumon a la plancha .")
                prix_plat=22

            elif choix_plat == 4:
                print("\n Vous avez choisi: la Boeuf bourguignon.")
                prix_plat=16
                



print(" \n les dessert")
print("1- creme brulée  \t 7 €")
print("2- Tiramissu     \t 8 €")
print("3- Glace au choix\t 9 €")
print("4- Panacota      \t 6 €")


choix_dessert = 0

while choix_dessert == 0:
    choix_dessert_str = input("\n Choisissez votre Dessert :   ")
    try:
        choix_dessert = int(choix_dessert_str)
    except:
        print("Veuiller entrer des chiffre !")
    else:
        if choix_dessert == 0:
            print("vous avez entrer la valeur 0 pouvez vous recommencer ?")
        elif choix_dessert > 4:
            print("Aucun choix correspondant")
            choix_dessert = 0
        elif choix_dessert < 0:
            print("Le chiffre choisi est négatif !!")
            choix_dessert = 0
        else:
            effacer_terminal()  

            if choix_dessert== 1 : 
                print("\n Vous avez choisi: la creme brulée  ")
                prix_dessert=7

            elif choix_dessert== 2:
                print("\n Vous avez choisi: le Tiramissu   ")
                prix_dessert=8

            elif choix_dessert == 3:
                print("\n Vous avez choisi: une Glace au choix   ")
                prix_dessert=9

            elif choix_dessert == 4:
                print("\n Vous avez choisi: un Panacota  ")
                prix_dessert=6
                

print("\n")
Total = prix_entree + prix_plat + prix_dessert
print("\n Total a payer : " ,Total,"€")
print("Au revoir !")