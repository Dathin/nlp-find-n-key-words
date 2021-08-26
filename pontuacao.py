PONTUACAO_SUBSTANTIVO = 1
PONTUACAO_DEMAIS = 0.1

palavras_pontuacoes = dict()

def pontuar_palavra(palavra: str, tipo: str) -> None:
    # ignorar pontuação de acentos restante da divisão das frases
    if len(palavra) >= 3:
        pontuacao = PONTUACAO_SUBSTANTIVO if tipo == 'NN' else PONTUACAO_DEMAIS
        if palavra in palavras_pontuacoes:
            palavras_pontuacoes[palavra] = palavras_pontuacoes[palavra] + pontuacao
        else:
            palavras_pontuacoes[palavra] = pontuacao
            

def exibir_pontuacao(numero_de_palavras_chave: int) -> None:
    lista_de_pontuacao = list()
    valores_ja_impressos = 0
    for key, value in palavras_pontuacoes.items():
        lista_de_pontuacao.append({'key': key, 'value': value})
    lista_de_pontuacao.sort(key=lambda x: x["value"], reverse=True)
    while valores_ja_impressos < numero_de_palavras_chave:
        print(f'{lista_de_pontuacao[valores_ja_impressos]["key"]}')
        valores_ja_impressos = valores_ja_impressos + 1