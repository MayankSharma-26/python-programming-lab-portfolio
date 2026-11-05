import math
print("Degree\tSin\t\tCos")
for degree in range(0, 361, 10):
    radian = math.radians(degree)
    sin_value = round(math.sin(radian), 4)
    cos_value = round(math.cos(radian), 4)
    print(f"{degree}\t{sin_value:.4f}\t\t{cos_value:.4f}")