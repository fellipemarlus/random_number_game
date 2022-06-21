#Biblioteca random importada para gerar o número aleatório
import random

# Função criada para gerar o número aleatório, com o método randint e o range de 1 até 20
def numeroGerado():
    return random.randint(1,20)

# Função criada para chamar o número aleatório, armazenar as tentativas e iniciar o chute.
def game():
    resposta = numeroGerado()
    tentativa = 0
    chute = 0
    while chute != resposta: # Enquanto o chute for diferente da resposta
        tentativa += 1 # Adiciona o valor + 1 na variável tentativa
        chute = int(input('Digite o seu chute: '))
        if chute > resposta:
            print('O chute foi acima do número sorteado\n')
        elif chute < resposta:
            print('O chute foi abaixo do número sorteado\n')
        else:
            print(f'Você acertou!! Você precisou de {tentativa} tentativas, e o número correto é {resposta}.')
            return False

print('''
         |-------------------------------------------------------|
         |----------- Bem vindo ao RANDOM NUMBER GAME -----------|
         |-------------------------------------------------------|
         |  Nesse jogo, você precisará advinhar um número entre  |
         |   1 e 20, se o chute for acima ou abaixo do número    |
         |       aleatório, o programa irá te dar dicas.         |
         |-------------------------------------------------------|

- INSTRUÇÕES PASSO A PASSO
- Será gerado um número aleatório, que está entre a sequência de 1 até 20.
- Você, deverá digitar um número, tentando advinhar qual número foi sorteado entre 1 e 20.
- O jogo irá ajudar, informando se o chute foi abaixo ou acima do número sorteado.\n''')

print('''Está pronto para jogar ? \n
Digite 1 para iniciar, ou digite 2 para jogar em outro momento.''')
start = int(input('Digite a opção: '))
print()

if start == 1:
    print('Número aleatório gerado\n')
    game()
elif start == 2:
    print('Programa encerrado, até a próxima!')
else:
    print('Opção inválida, programa encerrado.')



