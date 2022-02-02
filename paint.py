
# Paint Calculator
# Get User Input
length = int(input("Please Enter the Length of the Room in Feet: "))
width = int(input("Please Enter the Width of the Room in Feet: "))
height = int(input("Please Enter the Height of the Room in Feet: "))
doors = int(input("Please Enter the Number of Doors: "))
windows = int(input("Please Enter the number of Windows: "))

# Calculate and Print Results
wall_area = (2 * length * height) + (2 * width * height)
no_paint_area = 20 * doors + 15 * windows
paint_area = wall_area - no_paint_area
print("Total surface area to paint", paint_area)
gallons = wall_area / 350
gallons = round(gallons, 2)
print("Number of gallons of paint needed:", gallons)
