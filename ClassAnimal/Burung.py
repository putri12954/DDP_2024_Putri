from Animal import Animal
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,  paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu
        
    def info_burung(self):
        super().info_animal()
        print("paruh \t\t\t :", self.paruh,
              "\nWarna Bulu \t\t :", self.warna_bulu)
    
    
burung_beo = Burung("Beo", "Jagung", "Udara", "Bertelur", "Melengkung", "Biru")
burung_beo.info_burung()

print()
burung_beo = Burung("Merpati", "Beras", "Darat", "Bertelur", "lurus", "putih")
burung_beo.info_burung()


            