def kalkulator():
    print("Kalkulator Simpel Dibuat Oleh Frans")
    print("Pilih Operasi")
    print("1 Untuk Penjumlahan")
    print("2 Untuk Pengurangan")
    print("3 Untuk Perkalian")
    print("4 Untuk Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ['1','2','3','4']:
        angka1 = float(input("Masukkan angka pertama :"))
        angka2 = float(input("Masukkan angka kedua :"))

        if pilihan == '1' :
            hasil = angka1 + angka2
            print(f"Hasil Penjumlahan: {hasil}")
        elif pilihan == '2' :
            hasil = angka1 - angka2
            print(f"Hasil Pengurangan: {hasil}")
        elif pilihan == '3' :
            hasil = angka1 * angka2
            print(f"Hasil Pengkalian: {hasil}")
        elif pilihan == '4' :
            if angka2 != 0:
                hasil = angka1 / angka2
                print(f"Hasil Pembagian: {hasil}")
            else:
                print("Maaf, Pembagian tidak dapat dilakukan dengan angka 0")
    else:
        print("Maaf, Pilihan tidak tersedia!")

kalkulator()
