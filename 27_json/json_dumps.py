import json

dict_mahasiswa = {"nama":"Nursalim", 
    "npm":"201843500121", 
    "jurusan":"Teknik Informatika", 
    "ipk":3, 
    "blog":"https://www.masnursalim.com"}

json_mahasiswa = json.dumps(dict_mahasiswa)
print("=============== JSON String ===============")
print(json_mahasiswa)
print(type(json_mahasiswa)) 
