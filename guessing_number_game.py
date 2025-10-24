"""Objetivo: Integrar inputs, loop, número aleatório e dificuldade.
Mini Exercícios:
Gere o número secreto aleatório.


Peça para o usuário chutar o número usando o loop até acertar ou acabar as chances.


Dê feedback se o chute foi maior ou menor que o número secreto.


Ao final, mostre uma mensagem de vitória ou derrota com o número de tentativas.
"""

import random

print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
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

print(numero_aleatorio)
while not acertou and tentativa_atual < numero_tentativas: #enquanto ele não acertar ou enquanto a tentativa atual, nao chegar no numero de tentativas pré definido
    numero = int(input(f"Tentativa N{tentativa_atual+1}! Digite o seu chute: ")) #ir somando a tentativa atual
    if numero == numero_aleatorio: # se o número for igual ao número aleatório, gerar uma mensagem de acerto
        print(f"Você acertou, parabéns!")
        acertou = True
    else: #porem se o numero for diferente do numero aleatorio, gerar uma mensagem de erro
        print("Você errou :(")
    tentativa_atual += 1 #somar ao numero de tentativas
    
if acertou == False:
    print("Suas chances se esgotaram")