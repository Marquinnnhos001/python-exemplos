alunos= ['Viktor']
alunos.append('Carlos')
while True:
    nome = input('Digite o nome do Aluno: ')
    alunos.append(nome)
    resposta = input('Deseja Adicionar mais um Aluno? (S/N): ')
    if resposta.upper() == 'N':
        break
print("Alunos cadastrados: {alunos}")