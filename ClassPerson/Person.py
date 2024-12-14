class Person:
    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur
    def cetak(self):
        print("nama :\t\t\t", self.nama,
              "\ngender\t\t\t", self.gender,
              "\numur\t\t\t", self.umur)
        