import json

dict_mahasiswa = {"nama":"Nursalim", 
    "npm":"201843500121", 
    "jurusan":"Teknik Informatika", 
    "ipk":3, 
    "blog":"https://www.masnursalim.com"}

json_mahasiswa = json.dumps(dict_mahasiswa)
print("=============== JSON String tanpa ===============")
print(json_mahasiswa)

json_mahasiswa = json.dumps(dict_mahasiswa, indent = 8, separators=(".", "="))
print()
print("=============== JSON String dengan indent 8 dan separator . dan = ===============")
print(json_mahasiswa)
