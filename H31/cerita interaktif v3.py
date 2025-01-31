import random

def main():
    health = 100
    level = 1

    while health > 0:
        print(f"\nKesehatan Anda: {health}")
        print(f"Anda Memasuki Dungeon Level {level} Dan Bertemu Dengan Monster!")

        
        if level == 1:
            print("Monster yang muncul adalah Goblin!")
            print("1. Serang Goblin Dengan Pedang")
            print("2. Serang Goblin Dengan Busur")
            print("3. Mencoba Maju Dan Menghindari Goblin Tersebut")
        elif level == 2:
            print("Monster yang muncul adalah Serigala Liar!")
            print("1. Serang Serigala Dengan Pedang")
            print("2. Serang Serigala Dengan Busur")
            print("3. Mencoba Maju Dan Menghindari Serigala Tersebut")
        elif level == 3:
            print("Monster yang muncul adalah Naga Kecil!")
            print("1. Serang Naga Dengan Pedang")
            print("2. Serang Naga Dengan Busur")
            print("3. Mencoba Maju Dan Menghindari Naga Tersebut")
        else:
            print("Anda telah mencapai level tertinggi! Permainan berakhir.")
            break

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            if level == 1 and random.random() < 0.5:  # 50% peluang berhasil
                print("Kamu Berhasil Membunuh Goblin Tersebut!")
                level += 1
            elif level == 2 and random.random() < 0.4:  # 40% peluang berhasil
                print("Kamu Berhasil Membunuh Serigala Tersebut!")
                level += 1
            elif level == 3 and random.random() < 0.3:  # 30% peluang berhasil
                print("Kamu Berhasil Membunuh Naga Tersebut!")
                level += 1
            else:
                health -= 50
                print("Seranganmu Meleset Dan Monster Tersebut Berhasil Menyerangmu! -50 darah")
        
        elif choice == '2':
            if level == 1 and random.random() < 0.2:  # 20% peluang berhasil
                print("Seranganmu Kena Dan Membunuh Goblin Tersebut!")
                level += 1
            elif level == 2 and random.random() < 0.25:  # 25% peluang berhasil
                print("Seranganmu Kena Dan Membunuh Serigala Tersebut!")
                level += 1
            elif level == 3 and random.random() < 0.15:  # 15% peluang berhasil
                print("Seranganmu Kena Dan Membunuh Naga Tersebut!")
                level += 1
            else:
                health -= 15
                print("Seranganmu Meleset Dan Monster Tersebut Berhasil Menggoresmu! -15 darah")
        
        elif choice == '3':
            if random.random() < 0.1:  # 10% peluang berhasil
                print("Kamu Berhasil Mengelabui Monster Tersebut!")
            else:
                health -= 10
                print("Monster Tersebut Menangkapmu Dan Mendorong Kamu Kembali Ke Tempat Tadi! -10 darah")
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

    print("Anda telah mati. Permainan berakhir.")

if __name__ == "__main__":
    main()