class Mahasiswa:
    def __init__(self, nama, npm, jurusan, ipk):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
        self.ipk = ipk


# Membuat objek dari kelas Mahasiswa dengan nama nursalim
print("Data Objek sebelum di hapus properti ipk")
nursalim = Mahasiswa("Nursalim", "201843500121", "Teknik Informatika", 3.3)
print("Nama :", nursalim.nama)
print("NPM :", nursalim.npm)
print("Jurusan :", nursalim.jurusan)
print("IPK :", nursalim.ipk)

print("Data Objek setelah di hapus properti ipk")

# menghapus properti ipk dari objek nursalim
del(nursalim.ipk)
print("Nama :", nursalim.nama)
print("NPM :", nursalim.npm)
print("Jurusan :", nursalim.jurusan)

# akan error kalau mengakses properti yang sudah dihapus
# print("IPK :", nursalim.ipk)