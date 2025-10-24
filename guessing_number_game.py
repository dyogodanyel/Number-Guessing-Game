import random

print("BEM VINDO AO GUESSING NUMBER GAME")
print("Escolha o nível de dificuldade:")
print("Digite 1 para fácil")
print("Digite 2 para médio")
print("Digite 3 para dificil")

escolha_dificuldade = int(input("Nível: ")) #seleção de dificuldade
numero_tentativas = 0 #armazenar quantas chances vai ter disponível

if escolha_dificuldade not in [1, 2, 3]: # se nao for escolhido um dos 3 numeros
    print("NÚMERO INVÁLIDO! Usando nível médio.")
    numero_tentativas = 5 #estabelecido 5 chances do nivel medio
if escolha_dificuldade == 1: # se a escolha de dificuldade for 1
    numero_tentativas = 10 #some o numero de tentativas para 4
elif escolha_dificuldade == 2:
    numero_tentativas = 5
else:
    numero_tentativas = 3
    
print(f"Você tem {numero_tentativas} tentativas para acertar o número aleatório!")

numero_aleatorio = random.randint(0,20) #numero aleatorio nao altera dependendo da dificuldade
acertou = False
tentativa_atual = 0

mensagens_acerto = ["Parabéns!","Você acertou em cheio!","Belo chute!"] #todas as mensagem que podem aparecerem quando houver um acerto
mensagens_erro = ["Não foi dessa vez...","Você errou","Vish, tente mais uma vez"] #todas as mensagem que podem aparecerem quando houver um erro

dicas_maior = ["DICA: Chute mais alto!","DICA: Precisa aumentar","DICA: Tão pouco..."] #mensagem se o numero for maior que o numero aleatorio
dicas_menor = ["DICA: Chute mais baixo...","DICA: Precisa","DICA: É muito!"]#mensagem se o numero for menor que o numero aleatorio

print(numero_aleatorio)
while not acertou and tentativa_atual < numero_tentativas: #enquanto ele não acertar ou enquanto a tentativa atual, nao chegar no numero de tentativas pré definido
    print("******************************************")
    numero = int(input(f"    Tentativa de nº{tentativa_atual+1}\nDigite o numero que deseja adivinhar: ")) #ir somando a tentativa atual
    if numero == numero_aleatorio: # se o número for igual ao número aleatório, gerar uma mensagem de acerto
        print("******************************************")
        print(random.choice(mensagens_acerto))
        acertou = True
    else: #porem se o numero for diferente do numero aleatorio, gerar uma mensagem de erro
        print("******************************************")
        print(random.choice(mensagens_erro)) 
        if numero > numero_aleatorio: #mostrar dicas ao errar, mostrar que se o numero for maior que o numero aleatorio
            print(        random.choice(dicas_menor)) 
        else: #porem se usuario digitar numero menor
            print(        random.choice(dicas_maior)) 
    tentativa_atual += 1 #somar ao numero de tentativas
print(f"O número aleatório era {numero_aleatorio}")
if acertou == False:
    print("******************************************")
    print("                DERROTA\nVocê perdeu... deseja tentar novamente?")
else:
    print("******************************************")
    print("                VITÓRIA\nVocê acertou o número em cheio!")