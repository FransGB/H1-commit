def genap_ganjil(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

angka = int(input("Masukkan angka: "))
print(f"Angka {angka} adalah {genap_ganjil(angka)}.")