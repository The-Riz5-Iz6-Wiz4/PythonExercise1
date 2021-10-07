#Input
x1= float(input('Enter a value for x at point 1: '))
y1= float(input('Enter a value for y at point 1: '))
x2= float(input('Enter a value for x at point 2: '))
y2= float(input('Enter a value for y at point 2: '))

#Formula for slope of line

Slope= (y2-y1)/(x2-x1)

#Final output

print(f'The slope for a line that connects the two points ({y1},{x1}) and ({y2},{x2}) is', round(Slope, 5))