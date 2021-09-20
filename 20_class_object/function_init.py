class Mahasiswa:
    def __init__(self, nama, npm, jurusan, ipk):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
        self.ipk = ipk


# Membuat objek dari kelas Mahasiswa dengan nama nursalim
nursalim = Mahasiswa("Nursalim", "201843500121", "Teknik Informatika", 3.3)
print("Nama :", nursalim.nama)
print("NPM :", nursalim.npm)
print("Jurusan :", nursalim.jurusan)
print("IPK :", nursalim.ipk)