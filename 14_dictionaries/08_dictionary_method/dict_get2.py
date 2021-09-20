dict_mahasiswa = {"nama":"Nursalim", "npm":"201843500121", "jurusan":"Teknik Informatika", "ipk":3}

print("dict_mahasiswa :", dict_mahasiswa)

# menggunakan get() untuk mendapatkan nama, NPM, jurusan dan IP
print("Nama :", dict_mahasiswa.get("nama"))
print("NPM :", dict_mahasiswa.get("npm"))
print("Jurusan :", dict_mahasiswa.get("jurusan"))
print("IPK :", dict_mahasiswa.get("ipk"))

# Mencari value berdasarkan alamat yang tidak ada di dict menggunakan method get()
print("Alamat :", dict_mahasiswa.get("alamat"))

# Mencari value berdasarkan alamat yang tidak ada di dict menggunakan dict['key]
print("Alamat :", dict_mahasiswa["alamat"])