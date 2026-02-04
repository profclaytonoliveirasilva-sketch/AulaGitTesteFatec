nome = input("Digite o nome do aluno: ")

# Leitura da primeira prova com validação
while True:
    prova1 = float(input("Digite a nota da Prova 1 (0,0 a 10,0): ").replace(",", "."))
    if prova1 >= 0.0 and prova1 <= 10.0:
        break
    else:
        print("Nota inválida! Digite um valor entre 0.0 e 10.0.")

# Leitura da segunda prova com validação
while True:
    prova2 = float(input("Digite a nota da Prova 2 (0.0 a 10.0): ").replace(",", "."))
    if prova2 >= 0.0 and prova2 <= 10.0:
        break
    else:
        print("Nota inválida! Digite um valor entre 0.0 e 10.0.")

media = (prova1 + prova2) / 2

if media >= 6.0:
    status = "Aprovado"
else:
    status = "Reprovado"


print(f"\nAluno: {nome}")
print(f"Prova 01: {prova1:.1f}".replace(".", ","))
print(f"Prova 02: {prova2:.1f}".replace(".", ","))
print(f"Média: {media:.1f}".replace(".", ","))
print(f"Status: {status}")





