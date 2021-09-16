def fungsi_kali(n):
  return lambda a : a * n

kali_dua = fungsi_kali(2)
kali_tiga = fungsi_kali(2)

print("35 x 2 = ", kali_dua(35))
print("35 x 3 = ",kali_tiga(35))

print("100 x 2 = ", kali_dua(100))
print("100 x 3 = ",kali_tiga(100))