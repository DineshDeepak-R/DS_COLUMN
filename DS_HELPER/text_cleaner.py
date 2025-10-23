import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

class TextCleaner:
    def __init__(self, 
                 remove_stopwords=True, 
                 remove_fillers=True, 
                 do_lemmatize=True, 
                 to_lower=True):
        self.remove_stopwords = remove_stopwords
        self.remove_fillers = remove_fillers
        self.do_lemmatize = do_lemmatize
        self.to_lower = to_lower
        self.stop_words = set(stopwords.words('english'))
        self.filler_words = {"uh", "um", "like", "you know", "basically"}
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text: str) -> str:
        if self.to_lower:
            text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        if self.remove_fillers:
            tokens = [word for word in tokens if word not in self.filler_words]
        if self.remove_stopwords:
            tokens = [word for word in tokens if word not in self.stop_words]
        if self.do_lemmatize:
            tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        return " ".join(tokens)

    def clean_corpus(self, texts: list) -> list:
        return [self.clean_text(text) for text in texts]
    
if __name__ == "__main__":
    cleaner = TextCleaner()
    sample_text = "Um, I think this product is, like, really good!!! But you know, it’s a bit pricey."
    print("Original:", sample_text)
    print("Cleaned:", cleaner.clean_text(sample_text))
    corpus = ["Uh, this is an amazing movie!", "I like the acting, but um the plot was weak."]
    print("Cleaned Corpus:", cleaner.clean_corpus(corpus))