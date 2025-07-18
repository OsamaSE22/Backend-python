FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    Celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return Celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
#temp = float(input("Enter the temperature to convert: "))
while True:
    try:
        temp = float(input("Enter the temperature to convert: "))
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
measure = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if measure == 'F':
    result = convert_to_celsius(temp)
    print("{}°F is {}°C".format(temp, result))
elif measure == 'C':
    result = convert_to_fahrenheit(temp)
    print("{}°C is {}°F".format(temp, result))
else:
    print("Enter a valid unit.")
