
# Inicializa uma lista vazia para os convidados
convidados = []

# Solicita o nome de até 7 convidados
for i in range(1, 8):
    nome = input(f'Digite o nome do convidado {i}: ')
    convidados.append(nome)

# Pergunta se o usuário deseja remover um convidado
remover = input('Deseja remover algum convidado da lista? (sim/não): ').strip().lower()

if remover == 'sim':
    nome_remover = input('Digite o nome do convidado a ser removido: ')
    if nome_remover in convidados:convidados.remove(nome_remover)
        print(f'{nome_remover} foi removido da lista.')
    else:
        print(f'O convidado {nome_remover} não está na lista.')

# Exibe a lista final de convidados
print('Lista final de convidados:')
for convidado in convidados:
    print(convidado)