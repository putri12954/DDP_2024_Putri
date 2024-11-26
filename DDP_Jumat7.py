#restoran
print("## 1.RESTORAN ##")
print("Nama pembeli :")

#input
Nama =int(input(""" Nama anda:
    1.Putri
    2.Indah
    3.Clara
    masukan nama anda: """))
NoHP =int(input(""" No Hp:
    1.1111111111
    2.2222222222
    3.3333333333
    Masukan No Hp anda"""))
Menu =int(input(""" Menu Makanan:
    1.Nasi Goreng - 15.000
    2.Mie Goreng - 15.000
    3.Ayam Geprek - 18.000
    Masukan pilihan anda"""))

nomor = print(input("masukan pilihan: "))
#proses
if nomor == 1:
    totalmakan = porsi * 15.000
    print("Porsi Nasi Goreng = Rp", totalmakan)
    makan = ("Nasi Goreng")
elif nomor ==2:
    totalmakan = porsi * 12.000
    print("Porsi Mie Goreng = Rp", totalmakan)
    makan = ("Mie Goreng")
elif nomor == 3:
    totalmakan = porsi *18.000
    print("Ayam Geprek = Rp", totalmakan)
    makan = ("Ayam Geprek")
else:
    print("pilihan tidak ada, silahkan masukan lagi")
    



