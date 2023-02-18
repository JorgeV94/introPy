# 1 - import / bibliotecas

# 2 - Classes


# 3 - Métodos e Funções

# def = definition = definição

def print_hi(name):
    print(f'Oi, {name}') # a partir do Python 3
    print('oI, ' +  name) # antes do Python 3

def calcular_area_do_retangulo(largura,comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura,comprimento):
    return largura * comprimento/2

def contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de 0 até o fim
        print(numero) #exibir o numero
def apoiar_candidato(nome,vezes):
    for numero in range(vezes):
        #print(f'{numero} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>9}'.format(numero))

#def contagem_regressiva(inicio, fim):

#estrutura de identificação / execução do script
if __name__ == '__main__':
    resposta = "C"

    while resposta.upper() != 'Z':

        print('#####################################')
        print('#                                   #')
        print('#    M E N U   D E   O P Ç Õ E S    #')
        print('#                                   #')
        print('#    1 - Olá Mundo                  #')
        print('#    2 - Área do Retângulo          #')
        print('#    3 - Área do Quadrado           #')
        print('#    4 - Área do Triângulo          #')
        print('#    5 - Contagem Progressiva       #')
        print('#    6 - Apoiar Candidato           #')
        print('#    7 - Brincar de Plim            #')
        print('#                                   #')
        print('#    Z - Sair                       #')
        print('#                                   #')
        print('#####################################')

        resposta = input("Escolha sua opção")
        print(f'A sua escolha foi: {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Jorge')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(5, 4)
                print(f'A área do retângulo é de {resultado} m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(9)
                print(f'A área do quadrado é de {resultado} m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5, 10)
                print(f'A área do triângulo é de {resultado} m²')
            elif resposta == '5':
                contagem_progressiva(15)
            elif resposta == '6':
                apoiar_candidato('Tom', 5)
            elif resposta == '7':
                brincar_de_plim(8)
            else:
                print('Você digitou uma opção inválida. Escolha uma opção de 1 a 7')
        else:
            print("Você escolheu sair. Volte Sempre!")