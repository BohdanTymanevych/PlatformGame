import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos ):
        super().__init__()

        self.image = pygame.image.load('D:\PythonProjects\Test\download.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,100))
        self.rect = self.image.get_rect(topleft = pos)
        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -30

    def import_character_assets(self):
        character_path = '../graphics/character/'
        self.aniamations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}

        for animation in self.aniamations.keys():
            full_path = character_path + animation
            self.aniamations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.direction.y == 0:
            self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
