toko = {
    "1" : {"nama": "Manga", "Harga": 42000},
    "2" : {"nama": "Figur", "Harga": 150000},
    "3" : {"nama": "Novel", "Harga": 30000},
    "4" : {"nama": "Dakimakura", "Harga": 110000},
}

def tampilan_barang():
    print("daftar Barang:")
    for key, value in toko.items():
        print (f"{key}. {value['nama']} - RP {value['Harga']}")

def main():
    uang = int(input("Masukkan Jumlah Uang Yang Anda Miliki: RP "))

    while True:
        tampilan_barang

        pilihan = input("Pilih Barang yang ingin dibeli(Masukkan Nomor): ")

        if pilihan in toko:
            harga_barang = toko[pilihan]["Harga"]

            if uang >= harga_barang:
                uang -= harga_barang
                print(f"Anda telah membeli {toko[pilihan]['nama']} dengan harga Rp {harga_barang}")
                print(f"Sisa Uang Anda: Rp {uang}")
            else :
                print("Uang Anda tidak cukup untuk membeli barang ini")
        else:
            print("Pilihan Anda tidak ada di Toko!")

        lagi = input("Apakah Anda Ingin Membeli Lagi? (Ya/Tidak): ").lower()
        if lagi != 'Tidak':
            break

    print("Terima Kasih Telah Berbelanja di Toko Kami")

if __name__ == "__main__":
    main()
