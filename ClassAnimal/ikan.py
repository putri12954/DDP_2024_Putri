# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 
# buat minimal 2 objek untuk setiap class childnya. 

from Animal import Animal
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,  jenis_ikan, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_ikan = jenis_ikan
        self.ukuran = ukuran
        
    def info_ikan(self):
        super().info_animal()
        print("Jenis ikan \t\t :", self.jenis_ikan,
              "\nukuran \t\t\t :", self.ukuran)
    
    
Ikan_koki = Ikan("Koki", "Larva air", "Air", "Bertelur", "Tidak dapat dikonsumsi", "Kecil")
Ikan_koki.info_ikan()

print()
ikan_salmon = Ikan("Ikan Salmon", "ikan-ikan kecil", "Air", "Bertelur", "dapat dikonsumsi", "Besar")
ikan_salmon.info_ikan()


            