class Bilangan:
  def __iter__(self):
    self.cnt = 1
    return self

  def __next__(self):
    cnt = self.cnt
    self.cnt += 1
    return cnt

bil = Bilangan()
myiter = iter(bil)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))