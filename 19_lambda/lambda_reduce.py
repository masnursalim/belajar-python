# Menggunakan Lambda di dalam reduce()
from functools import reduce

bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hasil_jumlah = reduce((lambda x, y: x + y ), bilangan)
hasil_kali = reduce((lambda x, y: x * y ), bilangan)

print("Bilangan :", bilangan)
print("Hasil Jumlah :", hasil_jumlah)
print("Hasil Kali :", hasil_kali)