x = 1
print("logb (a) = x")
b = int(input("b = "))
a = int(input("a = "))
m = a
while m != b:
  x = x+1
  m = m/b
print("x = " + str(x))
