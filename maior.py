# 7. Crie função que retorne maior entre dois números.
def maior(a,b):
    if a > b:
        return a
    else:
        return b
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

resultado = maior (n1,n2)
print (f'O maior número digitado foi: {resultado}!')