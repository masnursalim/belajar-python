class Mahasiswa:
    def __init__(self, nama, npm, jurusan, ipk):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
        self.ipk = ipk


# Membuat objek dari kelas Mahasiswa dengan nama nursalim
print("Data objek nursalim sebelum dihapus")
nursalim = Mahasiswa("Nursalim", "201843500121", "Teknik Informatika", 3.3)
print("Nama :", nursalim.nama)
print("NPM :", nursalim.npm)
print("Jurusan :", nursalim.jurusan)
print("IPK :", nursalim.ipk)

# menghapus objek nursalim
del(nursalim)

print()
print("Mengakses objek nursalim setelah dihapus akan menampilkan error ")
print("Nama :", nursalim)