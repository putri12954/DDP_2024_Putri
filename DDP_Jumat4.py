# program menentukan bilangan ganjil dan genap
print("## 1. Program Bilangan Ganjil dan Genap ##")
print("========================")

#input bilangan 
bilangan = int(input("masukan bilangan anda: "))
#proses dan output
if bilangan % 2 ==0:
    print(bilangan, "merupakan bilangan genap ")
else:
    print(bilangan, "merupakan bilangan ganjil")

 # program menentukan nilai ujian
print("## 2. Program menentukan nilai ujian ##")
print("========================")

# input nilai
nilai_ujian = int(input("masukan nilai anda"))
#proses dan output
if nilai_ujian >= 75:
    print("kamu dinyatakan lulus")
else:
    print("kamu dinyatakan tidak lulus")

# program menentukan usia
print("## 3. Program menentukan usia ##")
print("========================")

# input usia
usia = int(input("masukan usia anda"))
#proses dan output
if usia >= 18:
    print("kamu dewasa")
elif usia >= 13 and usia <= 17:
    print("kamu remaja")
else:
    print("kamu anak-anak")

 # program cek keanggotaan
print("## 4. Program cek keanggotaan ##")
print("========================")

# input status
status_anggota = input("""daftar keanggotaan dibawah ini
1. gold
2. silver
3. bronze
masukan pilihan anda: """)

#proses dan output
if status_anggota == "gold" or status_anggota == "silver":
    print("selamat anda mendapatkan diskon.")
elif status_anggota == "bronze":
    print("maaf anda tidak mendapatkan diskon")
else:
    print("masukan kata yang benar")

# program menentukan diskon
print("## 1. Program menentukan diskon ##")
print("===============")

#input
jumlahpembelian = int(input("masukan jumlah pembelian anda :"))
#proses dan output
print(f"Anda mendapatkan diskon 10%") if jumlahpembelian > 100 else print("Anda tidak mendapatkan diskon")

 