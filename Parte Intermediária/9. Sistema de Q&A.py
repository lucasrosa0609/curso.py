perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '2', 'd': '6'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6', 'd': '24'},
        'resposta_certa': 'c',
    },
}


respostas_certas = 0
for pkey, pvalues in perguntas.items():
    print(f'{pkey}: {pvalues["pergunta"]}')

    print('Escolha as respostas abaixo: ')

    for rkey, rvalues in pvalues['respostas'].items():
        print(f'[{rkey}]:{rvalues}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pvalues['resposta_certa']:
        respostas_certas += 1
        print('Boa!')
    else:
        respostas_certas += 0
        print('Errou burro do caralho')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100



