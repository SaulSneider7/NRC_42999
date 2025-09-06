# pip install nltk
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Ver la version de nltk
print(nltk.__version__)

# nltk.download('punkt')
# nltk.download('punkt_tab')


texto = "Hola, me llamo Saul. Estoy aprendiendo a usar NLTK. Es una biblioteca muy útil."

# Tokenizamos en oraciones
oraciones = sent_tokenize(texto)
print("\nTokenizacion en oraciones:")
print(oraciones)

# Tokenizamos en palabras
palabras = word_tokenize(texto)
print("\nTokenizacion en palabras:")
print(palabras)
