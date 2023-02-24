# 1 - importação de pacotes
import json
import pytest
# 2 - Classe


# 3 - Definições (Funções e Métodos)

dados = {}
dados['cliente'] = [] # indica a criação de um vetor, matriz, lista ...
dados['cliente'].append({
    'nome':'Juca',
    'telefone':'11333648784',
    'email':'juca@iterasys.com.br'
})
dados['cliente'].append({
    'nome': 'Ana',
    'telefone': '213336487454',
    'email': 'ana@iterasys.com.br'

})
def criar_json():
    with open('clientes.json','w') as outfile:
        json.dump(dados,outfile, indent=4)
def ler_json():
    with open('clientes2.json') as outfile:
        dados = json.load(outfile)
        for registro in dados['cliente']:
            print('nome:  ' + registro['nome'])
            print('telefone:  ' + registro['telefone'])
            print('email:  ' + registro['email'])
            print('')
def ler_e_adicionar_json():
    with open('clientes2.json') as outfile:
        dados2 = json.load(outfile)
        temp = []
        for registro in dados2['cliente']:
            # exibir no console
            print('nome:  ' + registro['nome'])
            print('telefone:  ' + registro['telefone'])
            print('email:  ' + registro['email'])
            print('')
            #salvar na lista
            temp.append('\'nome\'' + ':' + '\'' + registro['nome'] + '\',' \
             + '\'telefone\'' + ':' + '\'' + registro['telefone'] + '\',' \
             +'\'email\'' + ':' + '\'' + registro['email'] + '\','
                        )
        dados['cliente'].extend(temp)
def testar_criar_json():
    criar_json()
    print(dados['cliente'])
def testar_ler_json():
    print('Leitura do JSON por linha / campo')
    ler_json()
def testar_ler_e_adicionar_json():
    ler_e_adicionar_json()
    print('Lista atualizada')
    print(dados['cliente'])

