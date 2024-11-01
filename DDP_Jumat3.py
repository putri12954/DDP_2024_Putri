# input
nama,nim,kelas,noTelp,alamat ="putri", "0110124228", "SI07", "085779695285", "JL.lenteg Agung Raya, No.20 RT.5/1 Lenteng Agung, Serengseng Sawah Jagakarsa,Jakarta Selatan"

#proses, output
print("Nama Mahasiswa:" ,nama)
print("Nim Mahasiswa:" ,nim)
print("Kelas Mahasiswa:" ,kelas)
print("Nomor Telpon Mahasiswa:" ,noTelp)
print("Alamat Mahasiswa:" ,alamat)

print()
print("No.2")
print()

# input
nama,nim,kelas,noTelp,alamat ="Siti Fatimah Azahra", "0110124228", "SI10", "085850052350", "JL.lenteg Agung Raya, No.20 RT.5/1 Lenteng Agung, Serengseng Sawah Jagakarsa,Jakarta Selatan"

#proses, output
print("Nama Mahasiswa:" ,nama)
print("Nim Mahasiswa:" ,nim)
print("Kelas Mahasiswa:" ,kelas)
print("Nomor Telpon Mahasiswa:" ,noTelp)
print("Alamat Mahasiswa:" ,alamat)

print()
print("No.3")
print()

#3. buat program python untuk mencari nilai berat badan ideal
#input
tb = int(input("Masukan Tinggi Badan:"))
#proses
bbIdeal = (tb-100)-((tb-100) *0.1)
#output
print("Badan badan ideal dengan tinggi badan adalah", bbIdeal, "kg")

print()
print("No.4")
print()

#input
celcius = float(input("Masukan nilai celcius:"))
#proses
fahreinheit = (celcius*9/5)+32
#output
print(celcius, "derajat celcius sama dengan", fahreinheit, "derajat fahereinteit")

print()
print("No.5")
print()

# Luas dan Volume Tabung
print("~~~~~~~~~~~~~Luas dan Volume Tabung~~~~~~~~~~~~~")
# input
jari_jari = input("masukan jari-jari tabung : ")
tinggi = input("masukan tinggi tabung : ")
phi = 3.14
# proses
volume = phi * int(jari_jari) * int(jari_jari) * int(tinggi)
luas = 2 * phi * int(jari_jari) * (int(jari_jari) + int(tinggi))
# output
print("luas tabung = ",luas)
print("volume tabung = ", volume)

