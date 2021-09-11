x = ["apel", "manggis", "jeruk"]
y = ["apel", "manggis", "jeruk"]
z = x

# bernilai True karena z sama dengan x
print(x is z)

# bernilai False karena berbeda (beda alamat memory) walaupun kontennya sama
print(x is y)

# membandingkan operator is dengan ==. Operator == hanya membandingkan nilai
print(x == y)

# bernilai False karena z sama dengan x
print(x is not z)

# bernilai True karena berbeda (beda alamat memory) walaupun kontennya sama
print(x is not y)