""" Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.

"""
notas = []

while True:
    entrada = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        
        else:
            print("Nota inválida! Digite um valor entre 0 e 10")
            continue
    except ValueError:
        print("Entrada inválida! Digite uma nota numérica ou 'fi'.")
if notas:
    media = sum(notas) / len(notas)
    print(f"\n Média da turma: {media: .2f}")
else:
    print("\n Nenhuma nota registrada.")