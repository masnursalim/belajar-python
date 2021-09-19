list_buah = ['Apel', 'Jeruk', 'Mangga', 'Pisang']
list_jenis = ['Washington', 'Santang', 'Manalagi', 'Ambon']
print("List Buah sebelum di extend :", list_buah)

list_buah.extend(list_jenis)
print("List Buah Favorit setelah di extend list_jenis :", list_buah)

list_mobil = ['Honda', 'Toyota', 'Suzuki', 'Mitsubishi']
print("List Mobil sebelum di extend :", list_mobil)
list_harga = [100000, 30000, 50000, 15000]
list_mobil.extend(list_harga)
print("List Mobil Favorit setelah di extend list_harga :", list_mobil)