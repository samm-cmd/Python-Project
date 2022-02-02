# Convert Inches to Cm
inches = int(input("Hello! Please Enter Distance in Inches: "))
cm = inches * 2.54
print(inches, "inches is equal to: ", cm, "cm")

# 2. Convert Pounds to Kilograms
weight = int(input("Please enter weight in Pounds: "))
kg = weight / 2.2
kg = round(kg, 2)
print(weight, "is equal to ", kg, "kg.")

# 3. Convert Temperature from Fahrenheit to celsius
temperature = int(input("Please Enter Temperature in Fahrenheit: "))
celsius = (temperature - 32) / 1.8000
celsius = round(celsius, 2)
print(temperature, "Fahrenheit is equal to: ", celsius, "celsius")
