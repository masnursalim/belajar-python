txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

# Return False karena mengandung line feed
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)