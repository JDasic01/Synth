import pygame
from sys import exit

class Key(pygame.sprite.Sprite):
    def __init__(self, type, pos_x, pos_y, note_position, notes):
        super().__init__()

        if type =='white_key':
            self.key = pygame.image.load('white_key.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x, pos_y]
            self.note_value = pygame.mixer.Sound(f'assets\\notes\\{notes[note_position]}.wav')
            self.note_position += 1 # global
        else:
            self.key = pygame.image.load('black_key.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x, pos_y]  
            self.note_value = pygame.mixer.Sound(f'assets\\notes\\{notes[note_position]}.wav') 
            self.note_position += 1

class Keyboard(pygame.sprite.Sprite, Key):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def draw_keyboard(num_of_keys):
        key_group = pygame.sprite.Group()
        # for key in range(num_of_keys):
        #     if key % 2 == 0:
        #         new_key = Key('white_key', pos_x, pos_y, note_position, notes)
        #         key_group.add(new_key)
        #     else:
        #         new_key = Key('black_key', pos_x, pos_y, note_position, notes)
        #         key_group.add(new_key)