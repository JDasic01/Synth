#
# This is Version 4
# Python script written by Cary Semar  8/21/2020
#   contact: lefty2000@verizon.net
# All command arguments are tab separated.
# The reader will stop if it encounters a blank line
# Static command:
#   set instruments for voices:
#   INS    v1  v2  v3 etc.
#   The first entry is a blank
# Dynamic Commands
#   A "#" sign indicates comment which is skipped by the reader
#   TEMPO   a   b
#   a = tempo in beats/minute
#   b = integer specifying length (in "ticks" of a quater note)
#
#   Set instrument voices for each channel
#       INS     v1      v2     v2 ...
#   Note commands:
#   column 1: duration of wait before next command (in ticks)
#   folloed by note keys e.g. C3# play 'C' octave 3, sharp
#
# 
import pygame
import pygame.time
import pygame.midi
import time
pygame.midi.init()
import os,sys,pdb
notes = {'REST': 0,
         'C1':36,'C1#':37,'D1':38,'D1#':39,'E1':40,'F1':41,
         'F1#':42,'G1':43,'G1#':44,'A1':45,'A1#':46,'B1':47,
         'C2':48,'C2#':49,'D2':50,'D2#':51,'E2':52,'F2':53,
         'F2#':54,'G2':55,'G2#':56,'A2':57,'A2#':58,'B2':59,
         'C3':60,'C3#':61,'D3':62,'D3#':63,'E3':64,'F3':65,
         'F3#':66,'G3':67,'G3#':68,'A3':69,'A3#':70,'B3':71,
         'C4':72,'C4#':73,'D4':74,'D4#':75,'E4':76,'F4':77,
         'F4#':78,'G4':79,'G4#':80,'A4':81,'A4#':82,'B4':83}
player = pygame.midi.Output(0)
channels = []
now_playing = []
volumes = []
bpm = 76
# bpm = 60*fps/ticks_per_beat
# fps = ticks_per_beat*bpm/60
ticks = 12  # 12 for a quarter note, 6 for eighth, 3 for sixteenth
fps = int(ticks*bpm/60.0)
dt = 0
volume = 127
def play(n,note):
    global now_playing
    ins = channels[n-1]
    player.set_instrument(ins)
    player.note_off(now_playing[n-1])
    if note != 0:
        player.note_on(note,volumes[n-1])
    now_playing[n-1] = note
def send_command(inrec):
    global fps,bpm,ticks,volumes
    inv = inrec.split('\t')
#    print inv
#    print 'length = ',len(inv)
    if inv[0] == 'INS':    # update channel setting
        n = len(inv)
        for i in range(n-1):
            if inv[i+1] != '':
                channels[i] = int(inv[i+1])
        return
        
    if inv[0] == 'TEMPO':

#        pdb.set_trace()
        bpm = int(inv[1])
        ticks = float(inv[2])
        fps = int(ticks*bpm/60.0)
        return
    if inv[0] == 'VOL':
        n = len(inv)-1
        for i in range(n):
            if inv[i+1] != '':
                volumes[i] = int(inv[i+1])
        return
    n = 0
    for col in inv:
#        print 'col,n',col,n
        if n == 0:
            dt = int(col)
#            print 'dt = ',dt
        else:
            if col != '':
#                print 'note = ',col
                note = notes[col]
                play(n,note)
        n = n + 1
    for t in range(dt):
        clock.tick(fps)
                
def load():
    global channels,volumes,now_playing,clock,fps
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print('Usage: python reader filename')
        exit()
#    pdb.set_trace()
    fd = open(fname,"r")
    while True:
        inrec = fd.readline()
        inrec = inrec.rstrip()
        print(inrec)
        inv = inrec.split('\t')
        if inrec[0] != '#':
            break
#    print inv
    for c in inv:
#        print 'c = ',c
        if c != 'INS':
            ins = int(c)
            channels += [ins]
            now_playing += [0]
            volumes += [127] # default volume is max
#    print 'There are ',len(channels),' instruments'
#    print 'voices = ',channels
    clock = pygame.time.Clock()
    t1 = pygame.time.get_ticks()
    print('t1 = ',t1/1000.0)
    running = True
    clock.tick(1)
    while running:
        inrec = fd.readline()
        inrec = inrec.rstrip()   # remove trailing newline
        print(inrec)
        if len(inrec) < 1:
            break
        if inrec[0] != '#':
            send_command(inrec)
        if len(inrec) == 0:
            running = False
        else:
            if inrec[0] == '':
                running = False
                print('shutdown')
    t2 = pygame.time.get_ticks()
    print('playing time = ',(t2-t1)/1000.0)
load()
print('fps = ',fps)
del player
pygame.midi.quit()

