x = input()
y = float(input())
z = (float(x) / (y**2))
if z < 18.5:
   print("Underweight")
elif (z >= 18.5) and (z < 25):
     print("Normal")
elif (z >= 25) and (z < 30):
     print("Overweight")
elif z >= 30:
     print("Obesity")