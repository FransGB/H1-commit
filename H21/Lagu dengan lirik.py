import pygame
import tkinter as tk 

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('H21/blue.mp3')
    pygame.mixer.music.play()
    lirik_label.config(text=lyric_text)

def stop_music():
    pygame.mixer.music.stop()
    lirik_label.config(text="")

lyric_text = """
Your morning eyes, I could stare like watching stars
I could walk you by, and I'll tell without a thought
You'd be mine, would you mind if I took your hand tonight?
Know you're all that I want this life

I'll imagine we fell in love
I'll nap under moonlight skies with you
I think I'll picture us, you with the waves
The ocean's colors on your face
I'll leave my heart with your air
So let me fly with you
Will you be forever with me?

My love will always stay by you
I'll keep it safe, so don't you worry a thing
I'll tell you I love you more
It's stuck with you forever, so promise you won't let it go
I'll trust the universe will always bring me to you

I'll imagine we fell in love
I'll nap under moonlight skies with you
I think I'll picture us, you with the waves
The ocean's colors on your face
I'll leave my heart with your air
So let me fly with you
Will you be forever with me?
"""
root = tk.Tk()
root.title("Lirik Lagu")
root.geometry("400x300")

lirik_label = tk.Label(root, text="", wraplength=350, justify="left")
lirik_label.pack(pady=20)

play_button = tk.Button(root, text="Putar Musik", command=play_music)
play_button.pack(pady=10)   

stop_button = tk.Button(root, text="Berhenti", command=stop_music)
stop_button.pack(pady=10)

root.mainloop()
