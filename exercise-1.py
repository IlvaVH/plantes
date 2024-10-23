# Original function
def convert_temperature(temperature, unit):
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                fahrenheit = (celsius * (9 / 5)) + 32
                if fahrenheit < -459.67:
                    # Invalid temperature, below absolute zero
                    return "Invalid temperature"
                else:
                    return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        if fahrenheit < -459.67:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = temperature + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return celsius, fahrenheit
    else:
        return "Invalid unit"


# Define new functions  to replace internals
def fahrenheit_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius


def celsius_to_kelvin(temperature):
    kelvin = temperature + 273.15
    return kelvin


def celsius_to_fahrenheit(temperature):
    fahrenheit = (temperature * (9 / 5)) + 32
    return fahrenheit


def kelvin_to_celsius(temperature):
    celsius = temperature - 273.15
    return celsius


# Modular function
def convert_temperature_modular(temperature, unit):
    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(temperature)
        if fahrenheit < -459.67:
            return "Invalid temperature"
        else:
            kelvin = celsius_to_kelvin(temperature)
            return fahrenheit, kelvin
    elif unit == "F":
        celsius = fahrenheit_to_celsius(temperature)
        if celsius < -273.15:
            return "Invalid temperature"
        else:
            kelvin = celsius_to_kelvin(celsius)
            return celsius, kelvin
    elif unit == "K":
        celsius = kelvin_to_celsius(temperature)
        if celsius < -273.15:
            return "Invalid temperature"
        else:
            fahrenheit = celsius_to_fahrenheit(celsius)
            return celsius, fahrenheit
    else:
        return "Invalid unit"


# Reported the same
convert_temperature(temperature=32, unit="F")
convert_temperature_modular(temperature=32, unit="F")

# Check invalid temperatures
convert_temperature(temperature=-300, unit="C")
convert_temperature_modular(temperature=-300, unit="C")
convert_temperature(temperature=-500, unit="F")
convert_temperature_modular(temperature=-500, unit="F")
convert_temperature(temperature=-1, unit="K")
convert_temperature_modular(temperature=-1, unit="K")

# Check invalid unit
convert_temperature(temperature=30, unit="M")
convert_temperature_modular(temperature=30, unit="M")
