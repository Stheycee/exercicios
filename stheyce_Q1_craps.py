from random import choice
lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4,5,6]
pontos = [4,5,6,8,9,10]
contadorJogadas = 0
ponto = 0
def jogaDados(lista1, lista2):
    dado1 = choice(lista1)
    dado2 = choice(lista2)
    result = dado1 + dado2
    
    return result


def encontraponto(ponto, contadorJogadas, valorDado):
    
    if valorDado == 7:
        print("Você tirou 7 e perdeu :(")
        
    while valorDado != 7:
        valorDado = jogaDados(lista1, lista2)
        print('Os dados rolaram e juntos deram: %i' %valorDado)
        contadorJogadas +=1
        if ponto == valorDado:
            print("Você jogou os dados %i vezes \nTirou %i e ganhou!!!" %(contadorJogadas, valorDado))
            break
        
    
        

    
while True:
    jogada = input("Quer jogar Craps? [S/N]: ")
    jogada = jogada.upper()
    if jogada == 'N':
        break
    valorDado = jogaDados(lista1, lista2)
    print('Os dados rolaram e juntos deram: %i' %valorDado)
    if valorDado == 7 or valorDado == 11:
        print("Você é um natural e ganhou!")
        break
    
    if valorDado == 2 or valorDado == 3 or valorDado == 12:
        print("CRAPS você perdeu!")
        break
    for i in pontos:
        if i == valorDado:
            contadorJogadas += 1
            ponto = i
            encontraponto(ponto, contadorJogadas, valorDado)
            break