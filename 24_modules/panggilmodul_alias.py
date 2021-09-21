import modulsaya as ms

# memanggil function yang ada di dalam module
ms.sayHello("Nursalim")

# memanggil variable dictionary mahasiswa
print("========== Data Mahasiswa ============")
print("Nama :", ms.mahasiswa["nama"])
print("NPM :", ms.mahasiswa["npm"])
print("Jurusan :", ms.mahasiswa["jurusan"])
print("IPK :", ms.mahasiswa["ipk"])
print("Blog :", ms.mahasiswa["blog"])