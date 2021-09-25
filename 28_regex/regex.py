import re

txt = "Belajar Python Sanag Menyenangkan Guys"
x = re.search("^Belajar.*Guys$", txt)

# jika ketemu
if x:
  print("Ya, Match banget")
else:
  print("Tidak Match")