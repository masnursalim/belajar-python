import json

# json string
json_str = '{ "nama":"Nursalim", "npm":"201843500121", "jurusan":"Teknik Informatika", "ipk":3.3, "blog":"https://www.masnursalim.com"}'

# parsing json string ke python dictionary
json_dict = json.loads(json_str)

# the result is a Python dictionary:
print(json_dict)
print(type(json_dict))

# Mengakses Data
print("======= Data Mahasiswa ============") 
print("Nama :", json_dict['nama'])
print("NPM :", json_dict['npm'])
print("Jurusan :", json_dict['jurusan'])
print("IPK :", json_dict['ipk'])
print("Blog :", json_dict['blog'])
