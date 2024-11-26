# #deklarasi fungsi
# def hai():
#     print("Hallo selamat datang di NF")
#     print()
# #panggil fungsi
# hai()
# hai()
# hai()  

#contoh2
def cetak(kata):
    print(kata)
cetak("hallo word")
cetak("selamat datang di NF")

def biodata(nama, alamat,umur):
    cetak("nama saya adalah"+ nama)
    cetak("alamat saya adalah"+ alamat)
    cetak("umur saya adalah"+str (umur))
biodata("putri", "Depok", 18)
    
def perkalian(angka1, angka2):
    cetak(angka1*angka2)
perkalian(3,4)
perkalian(10,10)

def Luas_persegi(sisi):
    cetak(sisi*sisi)
Luas_persegi(5)

def biodata(nama = "ahmad", alamat = "Depok",umur = 17):
    cetak("nama saya adalah" + nama)
    cetak("alamat saya adalah" + alamat)
    cetak("umur saya adalah" + str (umur))
biodata()

def angka1(x):
    return x*2
    