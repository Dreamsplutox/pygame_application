import pygame

pygame.init()

sananes_L = pygame.image.load('images/sananes_L.png')
sananes_R = pygame.image.load('images/sananes_R.png')



class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y - 12
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        if self.facing == -1:
            win.blit(sananes_L, (self.x, self.y))
        else:
            win.blit(sananes_R, (self.x, self.y))
