import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('D:\PythonProjects\Test\Хрипач Артем Генадійович.JPG').convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        #self.image = pygame.Surface((size, size))
        #self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift