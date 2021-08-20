import re
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.util import pr


class Preprocessor:
    def __init__(self, corpus_path, lang, to_lower=True) -> None:
        self._corpus_path = corpus_path
        self._lang = lang
        self._to_lower = to_lower

    def process(self):
        if self._lang == "eng":
            return self._eng_preprocess()
        elif self._lang == "bng":
            return self._bng_preprocess()

    def _eng_preprocess(self):
        with open(self._corpus_path, 'r') as reader:
            corpus = reader.read()

        # Clean from specific constructions
        corpus = corpus.replace('*', '')
        corpus = corpus.replace('_I_', 'I')
        corpus = corpus.replace('--', ' ')

        # Replace multiple newlines with dot to ease tokenization
        pattern = re.compile(r'\n{2,}')
        corpus = re.sub(pattern, '.', corpus)

        # Remove in sentence newlines
        corpus = corpus.replace('\n', ' ')
        corpus = ' '.join(corpus.split())

        if self._to_lower:
            corpus = corpus.lower()

        # Tokenize corpus into sentences
        # Discard those which are full uppercase (e.g. CHAPTER I) 
        # and only consist of a single character (those are just '.')
        corpus = sent_tokenize(corpus)
        corpus = [sent for sent in corpus if not sent.isupper() and len(sent) > 1]

        return corpus

    def _bng_preprocess(self):
        def _pp_bn_sent(line):
            cleanr = re.compile(r'[a-zA-Z<>0-9&;:=?"()\'/]+')
            line = re.sub(cleanr, '', line)
            clean_flags = re.compile(u'([\U0001F1E6-\U0001F1FF]{2})')
            line = re.sub(clean_flags, '', line)
            return line

        with open(self._corpus_path, 'r') as reader:
            corpus = reader.read()

        bn_corp = []
        corpus = corpus.replace("।", "\n").replace("!", "\n").replace("?", "\n").replace("<br />", "\n")
        for i, line in enumerate(corpus.split(sep="\n")):
           bn_corp.append(_pp_bn_sent(line))
        
        return bn_corp

    def split(self, corpus):
        corpus = list(filter(None, corpus))
        split_point = int(len(corpus)*0.8)
        train, test = corpus[:split_point], corpus[split_point:]
        print(len(train), len(test))

        with open(f"data/processed/{self._lang}_train.txt", 'w') as writer:
            for sent in train:
                writer.write(f"{sent}\n")

        with open(f"data/processed/{self._lang}_test.txt", 'w') as writer:
            for sent in test:
                writer.write(f"{sent}\n")

