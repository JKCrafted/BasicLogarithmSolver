print("logb (a) = x")
a = int(input("a = "))
x = int(input("x = "))
if a > 0:
  b = int(a**(1/x))
else:
  if x % 2 != 0: 
    m = int(a*(-1))
    b = int(m**(1/x))
    b = int(b*(-1))
  else:
    b = str("Undifined")
print("b = " + str(b))  
if b != "Undifined":
  if a > 0:
    if x % 2 == 0:
      print("and b = -" + str(b))
