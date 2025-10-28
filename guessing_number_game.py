import random
import time

def escolher_dificuldade(): #escolhendo dificuldade
    print("Bem vindo ao jogo de adivinhar o número!")
    print("A máquina está pensando em número entre 0 e 100.\n")
    print("Selecione o nível de dificuldade:")
    print("1 - Fácil (10 tentativas)")
    print("2 - Médio (5 tentativas)") 
    print("3 - Difícil (3 tentativas)\n")

    escolha_dificuldade = int(input("Digite a dificuldade desejada: ")) #seleção de dificuldade
    print("")
    numero_tentativas = 0 #armazenar quantas chances vai ter disponível
    
    
    if escolha_dificuldade == 1: 
        numero_tentativas = 10 
    elif escolha_dificuldade == 2:
        numero_tentativas = 5
    elif escolha_dificuldade == 3:
        numero_tentativas = 3
    else:
        print("Número invalido! Digite novamente")
    print(f"Você tem {numero_tentativas} tentativas para adivinhar o número correto\n")
    print("Vamos começar o jogo!")
    return numero_tentativas


def jogar_rodada(numero_tentativas): #funcao para o chute do numero, usa como parametro o numero de tentativas
    acertou = False
    tentativa_atual = 0
    numero_aleatorio = random.randint(0,100) #numero aleatorio nao altera dependendo da dificuldade
    while not acertou and tentativa_atual < numero_tentativas: #enquanto ele não acertar ou enquanto a tentativa atual, nao chegar no numero de tentativas pré definido
        print("")
        numero = int(input(f"Digite o seu chute: ")) #ir somando a tentativa atual
        if numero == numero_aleatorio: # se o número for igual ao número aleatório, gerar uma mensagem de acerto
            print(f"Parabéns! Você acertou o número correto em {tentativa_atual+1} tentativas")
            acertou = True
        else: #porem se o numero for diferente do numero aleatorio, gerar uma mensagem de erro
            if numero > numero_aleatorio: #mostrar dicas ao errar, mostrar que se o numero for maior que o numero aleatorio
                print(f"Errou! O número é menor que {numero}.") 
            else: #porem se usuario digitar numero menor
                print(f"Errou! O número é maior que {numero}.") 
        tentativa_atual += 1 #somar ao numero de tentativas
    return acertou #ao fim do loop, vai retornar se foi falso o chute ou verdadeiro



def tentar_novamente():
    resposta = input("Deseja jogar novamente? (Sim/Não): ") #perguntar se quer continuar
    if resposta.lower() == "sim": #se a respostaa for sim, retornar verdadeiro para a função
        return True
    else: #se nao, retornar falso para a funcao
        print("Fim de jogo! Obrigado por jogar!")
        return False

def main(): 
    jogar_novamente = True
    
    while jogar_novamente == True:
        numero_tentativas = escolher_dificuldade()
        resposta = jogar_rodada(numero_tentativas)
        jogar_novamente = tentar_novamente() #main funciona somente se a funcao tentar novamente for verdadeira

main()