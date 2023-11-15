import pygame


#definir la classe pour le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de la class
    def __init__(self,joueur):
        super().__init__()
        self.velocity = 5
        self.joueur = joueur
        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x +120
        self.rect.y = joueur.rect.y + 80
        self.origin_image = self.image
        self.angle = 0


    def rotation(self):
        #faire tourner le projectile
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.joueur.all_projectiles.remove(self)
        

    def move(self):
        self.rect.x += self.velocity
        self.rotation()
        #verifier si le projectile entre en collision avec un monstre
        for monstre in self.joueur.game.check_collision(self,self.joueur.game.all_monstres):
            #supprimer le projectile
            self.remove()
            #infiger des degats
            monstre.degat(self.joueur.attack)

    

        #Verifier si le projectile n est plus présent sur l ecran
        if self.rect.x > 1080:
            #Supprimer le projectile
            self.remove()
            #print("Projectile supprimé")






   
   


        

