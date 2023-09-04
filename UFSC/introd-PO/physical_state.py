#O estado físico das substâncias puras, como a água, depende da pressão e temperatura. Obtenha via entrada do usuário um valor de pressão p (em kPa) e uma temperatura T (em oC) e informe em qual estado físico encontra-se a água considerando-se as seguintes aproximações:
#Para p = 100 kPa = Sólido se T < 0oC; Mistura sólido-líquido se T = 0oC; Líquido se 0oC< T < 100oC; Mistura líquido-vapor se T = 100oC; Gasoso se T > 100oC
#Para p = 200 kPa = Mistura líquido-vapor se T = 120oC; Gasoso se T > 120oC
#Para p = 300 kPa = Mistura líquido-vapor se T = 133,6oC; Gasoso se T > 133,6oC
#Para p = 400 kPa = Mistura líquido-vapor se T = 143,6oC; Gasoso se T > 143,6oC  
#Para p = 500 kPa = Mistura líquido-vapor se T = 151,9oC; Gasoso se T > 151,9oC
#----------------------------------------------------------------------------------
#The physical state of the pure substances, like water, it depends on pressure and temperature. Get with user input  the pressure value in "p"(em kPa) and a temperature "t"(em oC) and inform what physical state is the water considering the temperatures:
#For p = 100 kPa = Solid state if T < 0°C; Solid-liquid mixture if T = 0°C; Liquid state if 0°C< T < 100°C; Liquid-vapor mixture if T = 100°C; Gaseous state if T > 100°C.
#For p = 200 kPa = Liquid-vapor mixture if T = 120°C; Gaseous state if T > 120°C.
#For p = 300 kPa = Liquid-vapor mixture if T = 133,6°C; Gaseous state if T > 133,6°C.
#For p = 400 kPa = Liquid-vapor mixture if T = 143,6°C; Gaseous state if T > 143,6°C.
#For p = 500 kPa = Liquid-vapor mixture if T = 151,9°C; Gaseous state if T > 151,9°C.
p = int(input('Report your value of pression: '))
t = int(input('Report your temperature °C: '))
if p == 100:
    if t < 0:
        print('Solid state.')
    elif t == 0:
        print('Solid-liquid mixture.')
    elif t > 0 and t < 100:
        print('liquid state.')
    elif t == 100:
        print('Liquid-vapor mixture.')
    elif t > 100:
        print('Gaseous state.')
elif p == 200:
    if t == 120:
        print('Liquid-vapor mixture.')
    elif t > 120:
        print('Gaseous state.')
elif p == 300:
    if t == 133.6:
        print('Liquid-vaper mixture.')
    elif t > 133.6:
        print('Gaseous state.')
elif p == 400:
    if t == 143.6:
        print('Liquid-vaper mixture.')
    elif t > 143.6:
        print('Gaseous state.')
elif p == 500:
    if t == 151.9:
        print('Liquid-vaper mixture.')
    elif t > 151.9:
        print('Gaseous state.')
