from math import*

AB = input("Длина первого катета")
AC = input("Длина второго  катета")

AB = float(AB)
AC = float(AC)

BC = sqrt(AB**2 + AC**2)

S = (AB * AC)/2
P = AB + AC + BC

print("Площадь треугольника:",S)
print("Периметр треугольника:",P)