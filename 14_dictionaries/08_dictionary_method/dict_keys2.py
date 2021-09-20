dict_mahasiswa = {"nama":"Nursalim", "npm":"201843500121", "jurusan":"Teknik Informatika", "ipk":3}

x = dict_mahasiswa.keys()

print("dictionary_keys awal :", x)

# menambahkan item baru yaitu blog
dict_mahasiswa["blog"] = "https://www.masnursalim.com"
print("dictionary_keys update :", x)