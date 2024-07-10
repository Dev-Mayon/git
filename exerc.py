#Crie um programa que identifique se existem numeros iguais em um vetor identificando qual numero é igual

vetor = []

for i in range (0,8):
    num = int(input(f'Digite o número do vetor{i + 1}: \n'))
    vetor.append(num)

print(f' O vetor digitado pelo usuário é {vetor}.\n')

contagem = {}

for num in vetor:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

repetidos = []

for num, count in contagem.items():
    if count > 1:
        repetidos.append((num,count))

if repetidos:
    for num, count in repetidos:
        print(f' O número {num} se repete {count} vezes(vez) no vetor.')
else:
    print('Não existem números que se repetem no vetor. ')



