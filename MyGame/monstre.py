import pygame
import random

class Monstre(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 90
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load("PygameAssets-main/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1,2)

    def degat(self, amount):
        # infliger des dégâts
        self.health -= amount

        # vérifier si le nouveau nombre de points de vie est inférieur ou égal à 0
        if self.health <= 0:
            # faire réapparaître un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 2)

    def maj_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # déplacement se fait que s'il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_joueurs):
            self.rect.x -= self.velocity
            print(f"Vélocité actuelle : {self.velocity}")

        # si le monstre est en collision avec le joueur
        else:
            # infliger des dégâts au joueur
            self.game.joueur.degat(self.attack)

    def update(self):
        # Appelez cette méthode dans la boucle principale du jeu pour mettre à jour la position du monstre
        self.forward()

        
        