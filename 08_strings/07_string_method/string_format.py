txt = "Beli Beras seharga {price:.2f} rupiah!"
print(txt.format(price = 10000))

txt1 = "Nama saya {fname}, umur {age} tahun".format(fname = "Nursalim", age = 30)
txt2 = "Nama saya {0}, umur {1} tahun".format("Nursalim",30)
txt3 = "Nama saya {}, umur {} tahun".format("Nursalim",30)
print(txt1)
print(txt2)
print(txt3)

txt = "We have {:<8} chickens."
print(txt.format(49))

txt = "We have {:>8} chickens."
print(txt.format(49))

txt = "We have {:^8} chickens."
print(txt.format(49))

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

txt = "The universe is {:,} years old."
print(txt.format(13800000000))

txt = "The universe is {:_} years old."
print(txt.format(13800000000))

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

txt = "We have {:d} chickens."
print(txt.format(0b101))

txt = "We have {:e} chickens."
print(txt.format(5))

txt = "We have {:E} chickens."
print(txt.format(5))

txt = "The price is {:.2f} dollars."
print(txt.format(45))
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))


x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))

