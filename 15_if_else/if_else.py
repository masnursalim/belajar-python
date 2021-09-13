a = 10
b = 15

print("Nilai a : ", a)
print("Nilai b : ", b)

if a > b:
  print("a lebih besar dari b")
elif a == b:
  print("a sama dengan b")
else:
  print("a lebih kecil dari b")

# shorthand if..else
print("a lebih besar dari b") if a > b else print("a sama dengan") if a == b else print("a lebih kecil dari b")  
