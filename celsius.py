# 8. Crie função que converta Celsius para Fahrenheit.
def converter(celsius): 
    fahrenheit = (celsius*9/5) + 32
    return fahrenheit
temperatura = float(input('Digite um valor em Celsius para converter em Fahrenheit: '))
resultado = converter(temperatura)
print (f'{temperatura}° equivale a {resultado}F')