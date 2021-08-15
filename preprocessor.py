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
        def _pp_bn_sent(line):
            cleanr = re.compile(r'[a-zA-Z<>0-9&;:=?"()\'/]+')
            line = re.sub(cleanr, '', line)
            clean_flags = re.compile(u'([\U0001F1E6-\U0001F1FF]{2})')
            line = re.sub(clean_flags, '', line)
            return line

        with open(self._corpus_path, 'r') as reader:
            corpus = reader.read()

        bn_corp = []
        corpus = corpus.replace("<br />", "\n").replace("।", "\n").replace("!", "\n").replace("?", "\n")
        for i, line in enumerate(corpus.split(sep="\n")):
           bn_corp.append(_pp_bn_sent(line))
        
        return bn_corp

    def split(self, corpus):
        corpus = list(filter(None, corpus))
        split_point = int(len(corpus)*0.8)
        train, test = corpus[:split_point], corpus[split_point:]
        print(len(train), len(test))

        with open(f"data/processed/{self._lang}_train.txt", 'w') as writer:
            writer.write("\n".join(train))

        with open(f"data/processed/{self._lang}_test.txt", 'w') as writer:
            writer.write("\n".join(test))
