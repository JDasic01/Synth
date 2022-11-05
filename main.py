import pygame
from pygame import midi
from sys import exit

def sin_osc(f, t, fs=22050):
    """
    Sintetizira sinusoidu željene frekvencije i trajanja.
    
    Argumenti:
        f - frekvencija sinusoide
        t - trajanje u sekundama
        fs - frekvencija uzorkovanja (opcionalno)
    """
    x = np.arange(0, t - 1/fs, 1/fs)
    return np.cos(2 * np.pi * f * x)

signal = sin_osc(440, 0.5)

def note2freq(midi_note):
    """Vraća frekvenciju koja odgovara MIDI noti."""
    return 440 * 2**((midi_note-69)/12)


pygame.init()
midi.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Synth')
clock = pygame.time.Clock()
print(f"Broj MIDI uređaja je {midi.get_count()}.")
midi_out = midi.Output(midi.get_default_output_id())
midi_out.note_on(55, channel=0, velocity=100)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)