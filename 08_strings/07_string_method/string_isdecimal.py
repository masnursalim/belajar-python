txt = "9"
x = txt.isdecimal()
print(x)

txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

txt = "10.5"
x = txt.isdecimal()
print(x)