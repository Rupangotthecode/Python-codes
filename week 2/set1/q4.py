input_list = [0, 20, 30, 40, 50]

fahrenheit_temps = list(map(lambda x: (x * 9/5) + 32, input_list))
celsius_temps = list(map(lambda x: (x - 32) * 5/9, fahrenheit_temps))


print("Celsius Temperatures: ", celsius_temps)
print("Fahrenheit Temperatures: ", fahrenheit_temps)