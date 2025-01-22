import random


hadiah = [
    "Common Weapon Accessories Skin ",  
    "Rare Weapon Accessories Skin",  
    "Epic Weapon Accessories Skin",  
    "Legend Weapon Accessories Skin",
    "Rare Uzi Skin",
    "Epic Vector45 Skin",
    "Legend H4 Skin"   
]


probabilitas = [50, 30, 15, 2, 5, 3, 1]

def gacha():
    hasil = random.choices(hadiah, weights=probabilitas, k=1)
    return hasil[0]

if __name__ == "__main__":
    while True:
        perintah = input("Ketik 'g' untuk melakukan undian 1x dan 'g10' untuk 10x (atau 'exit' untuk keluar): ").strip().lower()
        if perintah == "g":
            hadiah_terpilih = gacha()
            print(f"Selamat! Anda mendapatkan: {hadiah_terpilih}")
        elif perintah == "g10":
            print("Melakukan 10x gacha...")
            for i in range(10):
                hadiah_terpilih = gacha()
                print(f"Gacha {i + 1}: Anda mendapatkan: {hadiah_terpilih}")
        elif perintah == "exit":
            print("Terima kasih telah bermain!")
            break
        else:
            print("Perintah tidak dikenali. Silakan coba lagi.")