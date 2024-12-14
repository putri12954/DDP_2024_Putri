# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 
# buat minimal 2 objek untuk setiap class childnya. 

from Animal import Animal
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,  bisa, panjang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bisa = bisa
        self.panjang = panjang
        
    def info_ular(self):
        super().info_animal()
        print("Bisa \t\t\t :", self.bisa,
              "\nPanjang \t\t :", self.panjang)
    
    
ular_kebun = Ular("Ular Kebun", "Tikus", "Darat", "Bertelur", "Tidak Berbisa", "2,5 Meter")
ular_kebun.info_ular()

print()
ular_kobra = Ular("Ular Kobra", "Burung", "Darat", "Bertelur", "Berbisa", "1-3 Meter")
ular_kobra.info_ular()


            