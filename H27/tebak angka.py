import random

class TebakAngka:
    def __init__(self):
        self.angka_rahasia = random.randint(1, 50)
        self.tries = 0

    def tebak(self, angka):
        self.tries += 1
        if angka < self.angka_rahasia:
            return "Terlalu rendah!"
        elif angka > self.angka_rahasia:
            return "Terlalu tinggi!"
        else:
            return f"Selamat! Anda menebak angka {self.angka_rahasia} dalam {self.tries} percobaan."

permainan = TebakAngka()
while True:
    try:
        tebakan = int(input("Tebak angka antara 1 dan 50: "))
        hasil = permainan.tebak(tebakan)
        print(hasil)
        if "Selamat" in hasil:
            break
    except ValueError:
        print("Masukkan angka yang valid.")