import os.path

def ler_texto() -> str:
    with open(os.path.dirname(__file__) + '/../texto.txt', 'r') as file:
        return file.read();

def solicitar_numero_de_palavras_chave() -> int:
    numero_de_palavras_chave = input('Informe a quantidade desejada de palavras chave: ')
    try:
        return int(numero_de_palavras_chave)
    except:
        raise 'Quantidade de palavras chave desejadas deve ser um inteiro'