import pygame
from pygame import midi
from key import Keyboard
from sys import exit

# Setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Synth')

# MIDI setup
# midi.init()
# midi_out = midi.Output(midi.get_default_output_id())
# midi_in

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

keyboard = Keyboard()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.flip()
    keyboard.draw_keyboard(screen) #num of keys
    clock.tick(60)