from pontuacao import exibir_pontuacao, pontuar_palavra
from tratamento import tratar_texto
from leitor import ler_texto, solicitar_numero_de_palavras_chave
from entendimento import _dividir_em_frases
import nltk
from nltk import RSLPStemmer
# nltk.download('tagsets')

# Lẽ texto inserido no arquivo text.txt
texto = ler_texto()
numero_de_palavras_chave = solicitar_numero_de_palavras_chave()

texto_tratado = tratar_texto(texto)
frases_do_texto = _dividir_em_frases(texto_tratado)

for frase_do_texto in frases_do_texto:
    palavras_tokenizadas = nltk.tokenize.word_tokenize(frase_do_texto, language='portuguese') 
    palavras_tageadas = nltk.pos_tag(palavras_tokenizadas)
    for palavra_tageada in palavras_tageadas:
        pontuar_palavra(palavra_tageada[0], palavra_tageada[1])
exibir_pontuacao(numero_de_palavras_chave)