import pygame
from monstre import Monstre
from player import Joueur

# Cette classe représente notre jeu
class Game:

    def __init__(self):
        #definir si le jeux a commencer ou pas 
        self.is_playing = False
        #genere le joueur
        self.all_joueurs = pygame.sprite.Group()
        self.joueur = Joueur(self)
        self.all_joueurs.add(self.joueur)
        #groupe de monstre
        self.all_monstres = pygame.sprite.Group()
        self.pressed = {}
        

    
    def start(self):
        self.is_playing = True
        self.spawn_monstre()
        self.spawn_monstre()


    
    def game_over(self):
        #remettre le jeux a jour (retier les monstre ,la vie est le remettre en attente)
        self.all_monstres = pygame.sprite.Group()
        self.joueur.health = self.joueur.max_health
        self.is_playing = False


    def update(self, fenetre):
        # Appliquer l'image du joueur   
        fenetre.blit(self.joueur.image, self.joueur.rect)

        #actualiser la barre de vie du joueur
        self.joueur.maj_health_bar(fenetre)


        #recuperer les projectile du joueur
        for projectile in self.joueur.all_projectiles:
            projectile.move()

        #Appliquer l ensemble de l image de mon groupe de projectile
        self.joueur.all_projectiles.draw(fenetre)

        #verifier si le joueur veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.joueur.rect.x + self.joueur.rect.width < fenetre.get_width():
            self.joueur.move_right()
        
        elif self.pressed.get(pygame.K_LEFT) and self.joueur.rect.x > 0:
            self.joueur.move_left()

        #recuperer les monstre du jeux
        for monstres in self.all_monstres:
            monstres.forward()
            monstres.maj_health_bar(fenetre)


        #appliquer l ensemble des images de monstre 
        self.all_monstres.draw(fenetre)


    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)


    def spawn_monstre(self):
        monstre = Monstre(self)
        self.all_monstres.add(monstre)

       
