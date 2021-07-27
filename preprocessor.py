import re


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

        corpus = corpus.replace('*', '')
        corpus = corpus.replace('_I_', 'I')
        corpus = corpus.replace('--', ' ')

        if self._to_lower:
            corpus = corpus.lower()

        return corpus

    def _bng_preprocess(self):
        with open(self._corpus_path, 'r') as reader:
            corpus = reader.read()

        cleanr = re.compile(r'[a-zA-Z<>0-9&;:=?"()\'/]+')
        corpus = re.sub(cleanr, '', corpus)
        
        return corpus

    def split(self, corpus):
        split_point = int(len(corpus)*0.8)
        train, test = corpus[:split_point], corpus[split_point:]

        with open(f"data/{self._lang}_train.txt", 'w') as writer:
            writer.write(train)

        with open(f"data/{self._lang}_test.txt", 'w') as writer:
            writer.write(test)
