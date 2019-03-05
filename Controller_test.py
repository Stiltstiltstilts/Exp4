
import pygame.midi


pygame.midi.init()
devices = pygame.midi.get_count()
devices

input_dev = pygame.midi.get_default_input_id()

drum_pad = pygame.midi.Input(input_dev)

 # Starting polling
drum_pad.poll()

data = drum_pad.read(1)

for event in data:
    control = event[0]
    timestamp = event[1]
