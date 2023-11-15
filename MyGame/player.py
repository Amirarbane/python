import pygame
from projectile import Projectile

# Création de la classe pour notre joueur
class Joueur(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()  # Appel de la classe parent
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 16
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    
    def degat(self, amount):
        if self.health - amount > 0:
            self.health -= amount
        else:
            # si le joueur a plus de vie
            self.game.game_over()

        
        
    
           
    def maj_health_bar(self,surface):
       
       #dessiner la barre de vie
       pygame.draw.rect(surface, (60,63,60), [self.rect.x +50 , self.rect.y +20, self.max_health , 7])
       pygame.draw.rect(surface, (111,210,46), [self.rect.x +50 , self.rect.y +20, self.health, 7])
    
    def lancer_projectile(self):
        #cree une instance de la class Projectile
        self.all_projectiles.add(Projectile(self))

   
    def move_right(self):
        #si le joueur n est pas en colision avec un monstre
        if not self.game.check_collision(self,self.game.all_monstres):
         self.rect.x += self.velocity
        

    def move_left(self):
        self.rect.x -= self.velocity 