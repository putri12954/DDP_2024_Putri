#No1
#membuat sebuah funsi bernama celcius_ke_fahrenheit yang menerima satu argumen:suhu dalam celcius.
#fungsi ini harus mengembalikan  suhu yang dikonversi ke Fahrenheit.

def celcius_ke_fahrenheit(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

celcius1 = 0    
print(f"Hasilnya adalah {celcius_ke_fahrenheit(celcius1)}")
print(f"Hasilnya adalah {celcius_ke_fahrenheit(100)}")

print("--mencari nilai genap--")
#no2
# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
# print(is_genap(4))  # Output: True
# print(is_genap(7))  # Output: False

def is_genap(angka):
    hasil = angka % 2 == 0 
    return hasil

genap = 4
print(f" Output Dari Bilanga {genap} adalah {is_genap(genap)}")
print(is_genap(7))

print("--keterangan lulus dan tidak lulus--")
#no3
# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal

def Nilai_kelulusan(nilai):
    print()
    if nilai >= 80:
        return "lulus"
    else:
        return "gagal"
print(Nilai_kelulusan(80))
print(Nilai_kelulusan(60))

print("-----mencetak bilangan ganjil-----")
#no4
# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
# bilangan(20) # 1,3,5,7,9,11,13,15,17,19
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=" ")
bil_ganjil(20)