class Bilangan:
  def __iter__(self):
    self.cnt = 1
    return self

  def __next__(self):
    if self.cnt <= 20:
        x = self.cnt
        self.cnt += 1
        return x
    else:
        raise StopIteration

bil = Bilangan()
myiter = iter(bil)

for x in myiter:
    print(x)