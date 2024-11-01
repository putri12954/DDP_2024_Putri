#jenis kendaraan
kendaraan =["beat","motor",200,"pink",2]
print(kendaraan)

kendaraan.append("10jt")
print(kendaraan)

kendaraan.append("metic")
print(kendaraan)

kendaraan.insert(2,"Honda")
print(kendaraan)

kendaraan =["beat","motor",200,"pink",2]
print(kendaraan)

#menghitung luas
def hitung_luas():
    print("Pilih bangun datar untuk menghitung luas:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")

    pilihan = int(input("Masukkan pilihan (1/2/3): "))

    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi ** 2
            print(f"Luas persegi: {luas}")
        case 2:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = 3.14159 * (jari_jari ** 2)
            print(f"Luas lingkaran: {luas}")
        case 3:
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga: {luas}")
        case _:
            print("Salah pilih, silakan pilih 1, 2, atau 3.")

# Memanggil fungsi hitung_luas
hitung_luas()