# lambda dengan argument a akan ditambahkan 15
x = lambda a : a + 15
print("Nilai x(10) : ", x(10))  # hasilnya: 10 + 15
print("Nilai x(35) : ", x(35))  # hasilnya: 35 + 15


# lambda dengan dua argumen a dan b
# hasilnya a * b
x = lambda a, b : a * b
print(x(10, 30))
print(x(5, 5))