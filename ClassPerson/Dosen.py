from Person import Person
class Dosen(Person):
    gelar = ""
    jabatan = ""
    gaji = 0
    
    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
    def setGaji(self,uang):
        self.gaji += uang
    def cetak(self):
        super().cetak()
        print("Gelar\t\t\t:", self.gelar,
              "\njabata\t\t\t:", self.jabatan,
              "\nGaji\t\t\t", self.gaji,
              "\n----------------------")