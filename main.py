a = int(input("Līdz kuram skaitlim: "))
for i in range(a):
 print(i+1)
s = 0
for i in range(1, a+1):
  s = i + s
print("Summa ir", s)