# Impure function
def fahrenheit_to_celsius(temp_list, converted_temps=[]):
    for temp in temp_list:
        temp_c = (temp - 32.0) * (5.0/9.0)
        converted_temps.append(temp_c)
    return converted_temps

# Every time we run, it adds pieces
fahrenheit_to_celsius([32.0, 77.0])

# Pure function
def fahrenheit_to_celsius(temp_list, converted_temps=None):
    if converted_temps == None:
        converted_temps = []
    for temp in temp_list:
        temp_c = (temp - 32.0) * (5.0/9.0)
        converted_temps.append(temp_c)
    return converted_temps

# Every time we run, it adds pieces
fahrenheit_to_celsius([32.0, 77.0])
