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
def apoiar_canditado(nome,vezes):
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
    print_hi('Jorge')

    #chamar a função de calculo da area de retangulo

    resultado = calcular_area_do_retangulo(10,8)
    print(f'A area do retangulo é de {resultado} m2')

    #chamar a função de cálculo da area do quadrado
    resultado = calcular_area_do_quadrado(11)
    print(f'A area do quadrado é de {resultado} m2')

    #chamar a função do calculo da area do triangulo
    resultado = calcular_area_do_triangulo(15,26)
    print(f'A area do triangulo é de {resultado} m2')

    #executar uma contagem progressiva
    contagem_progressiva(29)

    #exibir o nome do canditado varias vezes
    apoiar_canditado('jorge',100)

    # brincar de plim
    brincar_de_plim(100)