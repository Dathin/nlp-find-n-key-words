import unidecode
import re
from nltk import corpus

def tratar_texto(texto : str) -> str:
    texto_minusculo = _tratamento_para_minusculo(texto)
    # texto_nao_acentuado = _tratamento_sem_acentuacao(texto_minusculo)
    texto_sem_numeros = _tratamento_sem_numeros(texto_minusculo)
    texto_sem_palavras_inuteis = _tratamento_sem_palavras_inuteis(texto_sem_numeros)
    return texto_sem_palavras_inuteis

def _tratamento_para_minusculo(texto: str) -> str:
    return texto.lower()
    
def _tratamento_sem_acentuacao(texto: str) -> str:
    return unidecode.unidecode(texto)

def _tratamento_sem_numeros(texto: str) -> str:
    return re.sub('\d', '', texto)

def _tratamento_sem_palavras_inuteis(texto: str) -> str:
    palavras_inuteis = corpus.stopwords.words("portuguese")
    texto_sem_palavras_inuteis = ''
    for palavra in texto.split(' '):
        if palavra not in palavras_inuteis:
            texto_sem_palavras_inuteis = texto_sem_palavras_inuteis + f' {palavra}'
    return texto_sem_palavras_inuteis

