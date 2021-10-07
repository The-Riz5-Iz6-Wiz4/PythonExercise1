import math

#Input
Side= float(input("Enter the length of the side of a hexagon: "))

#Calculations&Format

HexagonArea= ((3*math.sqrt(3))*(math.pow(Side, 2)))/2

FormatArea= format( HexagonArea, ".3f")

#Output

print(f"The area of a hexagon with side length {Side} is {FormatArea}")