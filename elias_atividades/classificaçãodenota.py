nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif 5 <= nota < 7:
    print("Recuperação")
else:
    print("Reprovado")