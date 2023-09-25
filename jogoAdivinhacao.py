import random
numeroAleatorio = random.randint(1, 100)
num1 = 1
num2 = 100
tentativas = 1

print('-----------------------------------')
print('    +++ JOGO DA ADIVINHAÇÃO +++    ')
print('-----------------------------------')
print('\nSeja bem-vindo(a) ao jogo da adivinhação!')

print(f'\nTentativa {tentativas}')
entradaUsuario = int(input(f'Para começar digite o seu palpite. Um número entre {num1} e {num2}: '))
while entradaUsuario != numeroAleatorio:
    tentativas = tentativas + 1
    if entradaUsuario < numeroAleatorio:
        num1 = entradaUsuario
    else:
        num2 = entradaUsuario
    print(f'\nTentativa {tentativas}')
    entradaUsuario = int(input(f'Digite um número entre {num1} e {num2}: '))
    
print(f'\nParabéns, você acertou! o número era -> {numeroAleatorio} <-\nE a quantidade de tentativas para acertar foram {tentativas}')