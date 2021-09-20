list_bilangan = [13, 8, 7, 9, 4, 12, 18, 21]
print("Bilangan :", list_bilangan)

bil_genap = list(filter(lambda x: (x%2 == 0) , list_bilangan))
print("Bilangan Genap :", bil_genap)

bil_ganjil = list(filter(lambda x: (x%2 != 0) , list_bilangan))
print("Bilangan Ganjil :", bil_ganjil)