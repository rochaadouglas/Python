#Converta um valor de temperatura informado pelo usuário e apresente o resultado da conversão para duas unidades de medida distintas. O usuário informa uma unidade de medida (Celsius, Fahrenheit ou Kelvin) e um valor de temperatura. Como saída, seu programa apresenta a conversão para as duas outras medidas. Caso o usuário informe algum tipo de medida diferente dos especificados, avise-o. Conversões: (oC=( oF -32)/1,8; oC=K -273; oF = (K-273)1,8+32)

#convert a value of temperature reported by user and show him the result. The user report an unit (Celsius, Fahrenheit or Kelvin) and a temperature value. As output, your program shows the conversion for two other measurements. If the user reports any different types of measurements, let them know.Conversions: (oC=( oF -32)/1,8; oC=K -273; oF = (K-273)1,8+32)
temperature = input('Report your current temperature, C = Celsius, F = Fahrenheit, K = Kelvin: ')
value_temperature = int(input('Report your value temperature: '))
if temperature != 'C' and temperature != 'F' and temperature != 'K':
    print('Temperature is not set correctly')
elif temperature == 'C':
    fahrenheit_temperature = (value_temperature*9/5) + 32
    kelvin_temperature = value_temperature + 273.15
    print(f'{fahrenheit_temperature:.1f}°Fahrenheit','and 'f'{kelvin_temperature:.1f}°Kelvin.')
elif temperature == 'F':
    celsius_temperature = (value_temperature - 32) * 5/9
    kelvin_temperature = (value_temperature - 32) * 5/9 + 273.15
    print(f'{celsius_temperature:.1f}°Celsius', 'and 'f'{kelvin_temperature:.1f}°Kelvin.')
elif temperature == 'K':
    celsius_temperature = value_temperature - 273.15
    fahrenheit_temperature = (value_temperature - 273.15) * 9/5 + 32
    print(f'{celsius_temperature:.1f}°Celsius', 'and 'f'{fahrenheit_temperature:.1f}°Fahrenheit.')