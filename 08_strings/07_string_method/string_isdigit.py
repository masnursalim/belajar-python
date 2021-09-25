txt = "12345"
x = txt.isdigit()
print(x)

txt = "0.123"
x = txt.isdigit()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())