def tampilkan_lirik(lagu):
    lirik = {
        "Yung Kai - Blue": """Lirik lagu Blue
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
Will you be forever with me?""",
        
        "Bruno Mars ft Rose - APT": """Lirik lagu APT
        [Intro]
Chaeyoung-iga joahaneun
Random game
Random game
Game start

[Chorus: ROSÉ]
Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh
Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh

[Verse 1: ROSÉ]
Kissy face, kissy face
Sent to your phone, but
I'm tryna kiss your lips for real (Uh-huh, uh-huh)
Red hearts, red hearts
That's what I'm on, yeah
Come give me somethin' I can feel, oh-oh, oh

[Pre-Chorus: ROSÉ]
Don't you want me like I want you, baby?
Don't you need me like I need you now?
Sleep tomorrow, but tonight, go crazy
All you gotta do is just meet me at the
See upcoming pop shows
Get tickets for your favorite artists

You might also like
ROSÉ & Bruno Mars - APT. (English Translation)
Genius English Translations
APT.
ROSÉ & Bruno Mars
Thick Of It
KSI

[Chorus: ROSÉ]
Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh
Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh

[Verse 2: Bruno Mars, ROSÉ, Bruno Mars & ROSÉ]
It's whatever (Whatever), it's whatever (Whatever)
It's whatever (Whatever) you like (Woo)
Turn this apateu into a club (Uh-huh, uh-huh)
I'm talkin' drink, dance, smoke, freak, party all night (Come on)
Geonbae, geonbae, girl, what's up? Oh-oh, oh

[Pre-Chorus: Bruno Mars & ROSÉ]
Don't you want me like I want you, baby?
Don't you need me like I need you now?
Sleep tomorrow, but tonight, go crazy
All you gotta do is just meet me at the

[Chorus: ROSÉ]
Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh
Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh

[Bridge: ROSÉ, ROSÉ & Bruno Mars]
Hey, so now you know the game
Are you ready?
'Cause I'm comin' to get ya, get ya, get ya
Hold on, hold on
I'm on my way
Yeah, yeah, yeah-yeah, yeah
I'm on my way
Hold on, hold on
I'm on my way
Yeah, yeah, yeah-yeah, yeah
I'm on my way

[Pre-Chorus: ROSÉ & Bruno Mars]
Don't you want me like I want you, baby?
Don't you need me like I need you now?
Sleep tomorrow, but tonight, go crazy
All you gotta do is just meet me at the

[Chorus: ROSÉ, Bruno Mars, ROSÉ & Bruno Mars]
Apateu, apateu
Apateu, apateu
Apateu, apateu
Just meet me at the (Uh, uh-huh, uh-huh)
Apateu, apateu
Apateu, apateu
Apateu, apateu
Just meet me at the (Uh, uh-huh, uh-huh)
Apateu, apateu
Apateu, apateu
Apateu, apateu
Just meet me at the (Uh, uh-huh, uh-huh)
Apateu, apateu
Apateu, apateu
Apateu, apateu
Uh, uh-huh, uh-huh""",
        
        "Billie Eilish - Birds of a Feathers": """Lirik lagu Birds of a Feathers...
        [Intro]
(But I wanna stay)

[Verse 1]
I want you to stay
'Til I'm in the grave
'Til I rot away, dead and buried
'Til I'm in the casket you carry
If you go, I'm goin' too, uh
'Cause it was always you (Alright)
And if I'm turnin' blue, please don't save me
Nothin' left to lose without my baby

[Refrain]
Birds of a feather, we should stick together, I know
I said I'd never think I wasn't better alone
Can't change the weather, might not be forever
But if it's forever, it's even better

[Pre-Chorus]
And I don't know what I'm cryin' for
I don't think I could love you more
It might not be long, but baby, I

[Chorus]
I'll love you 'til the day that I die
'Til the day that I die
'Til the light leaves my eyes
'Til the day that I die
See Billie Eilish Live
Get tickets as low as $143

You might also like
Houdini
Eminem
True Blue (Demo)
Billie Eilish
WILDFLOWER
Billie Eilish
[Verse 2]
I want you to see, hm
How you look to me, hm
You wouldn't believe if I told ya
You would keep the compliments I throw ya
But you're so full of shit, uh
Tell me it's a bit, oh
Say you don't see it, your mind's polluted
Say you wanna quit, don't be stupid

[Pre-Chorus]
And I don't know what I'm cryin' for
I don't think I could love you more
Might not be long, but baby, I
Don't wanna say goodbye

[Chorus]
Birds of a feather, we should stick together, I know ('Til the day that I die)
I said I'd never think I wasn't better alone ('Til the light leaves my eyes)
Can't change the weather, might not be forever ('Til the day that I die)
But if it's forever, it's even better

[Post-Chorus]
I knew you in another life
You had that same look in your eyes
I love you, don't act so surprised"""
    }
    
    return lirik.get(lagu, "Lagu tidak ditemukan.")

def main():
    print("Pilih lagu yang ingin ditampilkan liriknya:")
    print("1. Yung Kai - Blue")
    print("2. Bruno Mars ft Rose - APT")
    print("3. Billie Eilish - Birds of a Feathers")
    
    pilihan = input("Masukkan nomor pilihan (1/2/3): ")
    
    if pilihan == "1":
        lagu = "Yung Kai - Blue"
    elif pilihan == "2":
        lagu = "Bruno Mars ft Rose - APT"
    elif pilihan == "3":
        lagu = "Billie Eilish - Birds of a Feathers"
    else:
        print("Pilihan tidak valid.")
        return
    
    lirik = tampilkan_lirik(lagu)
    print("\nLirik dari", lagu, "adalah:")
    print(lirik)

if __name__ == "__main__":
    main()