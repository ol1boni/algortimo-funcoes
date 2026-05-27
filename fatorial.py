def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
n1 = int(input('Digite um número para calulcar o fatorial: '))
print (fatorial(n1))