from Person import Person
class Mahasiswa(Person):
    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester
    def cetak(self):
        super().cetak()
        print("Prodi\t\t\t:",self.prodi,
              "\nSemester\t\t",self.semester)