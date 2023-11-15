import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

if not nltk.corpus.stopwords.words():
    nltk.download('stopwords')

if not nltk.corpus.wordnet.words():
    nltk.download('wordnet')

if 'omw-1.4' not in nltk.data.path:
    nltk.download('omw-1.4')

def remove_non_alphanumeric(text):
    """
    Remove caracteres não alfanuméricos de um texto.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def to_lowercase(text):
    """
    Converte todo o texto para minúsculas.
    """
    return text.lower()

def remove_stopwords(text, language='portuguese'):
    """
    Remove stopwords do texto.
    """
    stop_words = set(stopwords.words(language))
    return ' '.join([word for word in text.split() if word not in stop_words])

def stem_text(text, language='portuguese'):
    """
    Aplica stemming ao texto.
    """
    stemmer = SnowballStemmer(language)
    return ' '.join([stemmer.stem(word) for word in text.split()])

def lemmatize_text(text):
    """
    Aplica lematização ao texto.
    """
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

# Função de pré-processamento que combina todas as etapas acima
def preprocess_text(text, remove_stopwords_flag=True, use_stemming=False):
    text = remove_non_alphanumeric(text)
    text = to_lowercase(text)
    if remove_stopwords_flag:
        text = remove_stopwords(text)
    if use_stemming:
        text = stem_text(text)
    else:
        text = lemmatize_text(text)
    return text
