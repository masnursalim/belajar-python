# membuat kelas parent yaitu kelas Manusia
class Manusia():
    def __init__(self, nama, jns_kelamin, alamat):
        self.nama = nama
        self.jns_kelamin = jns_kelamin
        self.alamat = alamat

    def say_hello(self):
        print("Hallo nama saya",self.nama)

# Membuat object
m1 = Manusia("Nursalim", "Laki-Laki", "Brebes")
m2 = Manusia("Indah", "Perempuan", "Jakarta")

m1.say_hello()
m2.say_hello()

