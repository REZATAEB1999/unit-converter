def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("TEMPERATURE CONVERTER")
choice = input("Convert (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius? ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print("Temperature in Fahrenheit:", round(f, 2))
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print("Temperature in Celsius:", round(c, 2))
else:
    print("Invalid choice.")
