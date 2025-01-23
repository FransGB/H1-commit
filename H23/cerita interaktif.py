class Character:
    def __init__(self, strength=5, intelligence=5, charisma=5):
        self.strength = strength
        self.intelligence = intelligence
        self.charisma = charisma

    def display_attributes(self):
        print(f"Strength: {self.strength}, Intelligence: {self.intelligence}, Charisma: {self.charisma}")

def main():
    print("Dani the Rizzler")
    player = Character()

    print("\nDisaat Dani Sedang Keluar Kos Untuk Mencari Makan, Dijalan Dia Tidak Sengaja Bertemu Dengan Gadis Kecil Yang Keliatannya Berumur 10 Tahun")
    print("Dani Langsung Jatuh Cinta Dengan Anak Kecil Itu Dan Mencoba Mendekatinya")
    player.display_attributes()

    while True:
        print("\nApa yang Akan Dani Lakukan?")
        print("1. Membawa Lari Gadis Kecil Itu Ke Kos.")
        print("2. MengRizz Gadis Tersebut Dengan 'Rawrrrr'")
        print("3. Memanupilasi Gadis Kecil Tersebut.")
        print("4. Keluar dari permainan.")

        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            if player.strength >= 6:
                print("Dani berhasil Membawa Gadis Kecil Tersebut Ke Dalam Kos!")
                player.intelligence += 1  
            else:
                print("Dani Tidak Sanggup Mengangkat Gadis Kecil Tersebut!")
                player.strength += 1  

        elif choice == '2':
            if player.charisma >= 6:
                print("Gadis Kecil Itu Berhasil Terkena Rizz Lvl100 Dani")
                player.intelligence += 2  
            else:
                print("Gadis Kecil Itu Takut Melihat Dani.")
                player.charisma += 1  

        elif choice == '3':
            if player.intelligence >= 6:
                print("Dani Berhasil Memanupilasi Gadis Kecil Tersebut Masuk Kedalam Kos!")
                player.strength += 1  
            else:
                print("Gadis Kecil Tersebut Berpikir Jika Dani Tidak Sigma.")
                player.intelligence += 1  

        elif choice == '4':
            print("Terima kasih telah bermain!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

        player.display_attributes()

if __name__ == "__main__":
    main()