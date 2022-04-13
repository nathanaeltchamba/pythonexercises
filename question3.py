places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]


to_farenheit = lambda data: (data[0], data[1]*(9/5)+32)

temp_conversation = list(map(to_farenheit,places))

print(temp_conversation)




# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION
# F = C * 9/5 + 32
