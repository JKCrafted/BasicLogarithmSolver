print("logb (a) = x")
b = int(input("b = "))
x = int(input("x = "))
m = 1
a = b
while m != x:
  a = a*b
  m = m+1
print("a = " + str(a))
