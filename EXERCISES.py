#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.

nota_aluno = float(input("Digite uma nota entre 0 e 10: "))

while nota_aluno < 0 or nota_aluno > 10:
    nota = float(input("Valor inválido. Digite uma nota entre 0 e 10: "))

print("Nota válida")

#Faça um programa que leia 5 números e informe o maior número.

cont = 0
lista_numeros =[]
while cont != 5:
    numero = int(input('Digite um numero: '))
    lista_numeros.append(numero) #Acrescenta número na lista antes criada
    cont = cont + 1

maior = max(lista_numeros) # Retorna o numero máximo em uma lista
print("O maior valor declarado é", maior)

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for numero_impar in range (1, 51):
    if(numero_impar % 2 == 1):
        print (numero_impar)

#Faça um programa que leia 5 números e informe a soma e a média dos números.

cont = 0
lista_numeros =[]
while cont != 5:
    numero = int(input('Digite um numero: '))
    lista_numeros.append(numero) #Acrescenta número na lista antes criada
    cont = cont + 1

soma_valores = sum(lista_numeros)
media_valores = sum(lista_numeros) / 5
print("A soma total dos valores é", soma_valores)
print("A média dos valores é", media_valores)

#Faça um programa que calcule o número médio de alunos por turma. 
#Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

qtde_turmas = int(input("Insira o número de turmas "))
alunos_por_turma = []

for i in range(qtde_turmas):
    qtde_alunos = int(input("Insira o número de alunos "))
    if qtde_alunos <= 40:
        qtde_turmas += 1
        alunos_por_turma.append(qtde_alunos)
    if qtde_alunos > 40:
        break

media = sum(alunos_por_turma) / len(alunos_por_turma)
print("A media de alunos por turma é: ", media)



#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

numero_eleitores = int(input("Insira o número de eleitores participantes: "))
valores_votos = [] #Inicializa a lista

for i in range(numero_eleitores):
    votante = valores_votos.append(int(input("Qual candidato deseja votar? [1, 2, 3]: ")))

print("Quantidade de votos para candidato 1: ", valores_votos.count(1))
print("Quantidade de votos para candidato 2: ", valores_votos.count(2))
print("Quantidade de votos para candidato 3: ", valores_votos.count(3))