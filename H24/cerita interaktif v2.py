import random

def main():
    health = 100

    while health > 0:
        print(f"\nKesehatan Anda: {health}")
        print("Anda Memasuki Dungeon Dan Bertemu Dengan Monster!")
        print("1. Serang Monster Dengan Pedang")
        print("2. Serang Monster Dengan Busur")
        print("3. Mencoba Maju Dan Menghindari Monster Tersebut")
        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            if random.random() < 0.5:  # 10% peluang berhasil
                print("Kamu Berhasil Membunuh Monster Tersebut!")
            else:
                health -= 50
                print("Seranganmu Meleset Dan Monster Tersebut Berhasil Menyerangmu! -50 darah")
        
        elif choice == '2':
            if random.random() < 0.2:  # 20% peluang berhasil
                print("Seranganmu Kena Dan Membunuh Monster Tersebut!")
            else:
                health -= 15
                print("Seranganmu Meleset Dan Monster Tersebut Berhasil Menggoresmu! -15 darah")
        
        elif choice == '3':
            if random.random() < 0.1:  # 50% peluang berhasil
                print("Kamu Berhasil Mengelabui Monster Tersebut!")
            else:
                health -= 10
                print("Monster Tersebut Menangkapmu Dan Mendorong Kamu Kembali Ke Tempat Tadi! -10 darah")
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

    print("Anda telah mati. Permainan berakhir.")

if __name__ == "__main__":
    main()