txt = "Python"
x = txt.isidentifier()
print(x)

txt = "123Python"
x = txt.isidentifier()
print(x)

txt = "Python123"
x = txt.isidentifier()
print(x)

txt = "_Python"
x = txt.isidentifier()
print(x)