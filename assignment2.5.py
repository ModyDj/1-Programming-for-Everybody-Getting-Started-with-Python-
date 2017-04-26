'''
Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted
temperature.
'''
cel = raw_input("Enter the Celsius temperature:")
fah = float(cel) * 9.0 / 5.0 + 32
print "Fahrenheit temperature is %.2f" %fah