import pygame
import time 

pygame.mixer.init()
pygame.mixer.music.load('H20/igloo.mp3')
pygame.mixer.music.play()

print("Tekan b untuk Berhenti")
while pygame.mixer.music.get_busy():
    user_input = input()
    if user_input.lower()=='b':
        pygame.mixer.music.stop()
        print("Musik Berhenti")
        break