#input, v for velocity, a for acceleration
v = float(input("Enter the plane's take off speed in m/s: "))
a = float(input("Enter the plane's acceleration in m/s^2: "))

#Formula for min runway length

Runway = (v**2)/(2*a)

#Output

print("The minimum runway length for this airplane is", round(Runway, 4), "meters")