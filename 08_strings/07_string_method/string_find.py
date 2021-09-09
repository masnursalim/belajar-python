txt = "Belajar Python sangat menyenangkan!"

x = txt.find("a")
print(x)

x = txt.find("a", 5, 10)
print(x)

print(txt.find("q"))
print(txt.index("q"))