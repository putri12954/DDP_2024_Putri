from Mahasiswa import Mahasiswa
from Dosen import Dosen

d1 = Dosen("Amira", "Wanita", 35, "S.Si, M.Kom", "LPPM" )
d2 = Dosen("Martin", "Pria", 45, "S.Si, M.Kom", "LTSI" )
m1= Mahasiswa("Putri", "wanita", 18, "Sistem Informasi", 1)
m2 = Mahasiswa("Muhamad Yusuf", "Pria", 21, "Teknik Informatika", 5)

d1.setGaji(12000000)
d2.setGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()