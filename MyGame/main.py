import pygame
import math
from game import Game
pygame.init()




pygame.display.set_caption("Mon jeux By Amir")
fenetre = pygame.display.set_mode((1080, 720))  # Définition de la fenêtre

background = pygame.image.load('PygameAssets-main/bg.jpg')

#importer la banniere
banniere = pygame.image.load("PygameAssets-main/banner.png")
banniere = pygame.transform.scale(banniere,(500,500))
banniere_rect = banniere.get_rect()
banniere_rect.x = math.ceil(fenetre.get_width() /4)

#importer le bouton pour lancer le jeu
play_button = pygame.image.load("PygameAssets-main/button.png")
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x =  math.ceil(fenetre.get_width() /3.33)
play_button_rect.y = math.ceil(fenetre.get_height() /2) 



#charger le jeux
game = Game()

clock = pygame.time.Clock()
running = True



while running:

    #limite de 120 image par seconde
    clock.tick(120)

    # Afficher l'image de fond
    fenetre.blit(background, (0, -200))

    # Vérifier si le jeu a commencé ou pas
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(fenetre)

        # Mettre à jour la position des monstres
        for monstre in game.all_monstres:
            monstre.forward()

    # Vérifier si le jeu n'a pas commencé
    else:
        # Ajouter l'écran de bienvenue
        fenetre.blit(play_button, play_button_rect)
        fenetre.blit(banniere, banniere_rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si la touche espace est pressée
            if event.key == pygame.K_SPACE:
                game.joueur.lancer_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si la souris est en collision avec le bouton
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode lancer
                game.start()

          


            

    
    
    

