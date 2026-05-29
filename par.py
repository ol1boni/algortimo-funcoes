# 5. Crie função que verifique número par ou ímpar.
def par (a):
    if a%2 == 0:
        return f'{a} é par'
    else:
        return f'{a} é ímpar'
n1 = float(input('Digite um númro para verficar se é par ou ímpar: '))
print (par(n1))