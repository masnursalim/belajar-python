import modulsaya

# memanggil function yang ada di dalam module
modulsaya.sayHello("Nursalim")

# memanggil variable dictionary mahasiswa
print("========== Data Mahasiswa ============")
print("Nama :", modulsaya.mahasiswa["nama"])
print("NPM :", modulsaya.mahasiswa["npm"])
print("Jurusan :", modulsaya.mahasiswa["jurusan"])
print("IPK :", modulsaya.mahasiswa["ipk"])
print("Blog :", modulsaya.mahasiswa["blog"])