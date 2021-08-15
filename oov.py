from collections import Counter

from nltk.util import pr


class OOV:
    def __init__(self, lang="eng") -> None:
        self._train_path = f"./data/processed/{lang}_train.txt"
        self._test_path = f"./data/processed/{lang}_test.txt"
        self._train_vocab = Counter()
        self._test_vocab = Counter()

        self._init_baseline()
        self._baseline_rate()

    def _init_baseline(self):
        with open(self._train_path, 'r') as reader:
            for line in reader:
                words = [self._clean_word(word) for word in line.split()]
                self._train_vocab.update(words)

        with open(self._test_path, 'r') as reader:
            for line in reader:
                words = [self._clean_word(word) for word in line.split()]
                self._test_vocab.update(words)

    def _clean_word(self, word):
        temp = word

        while word and not word[0].isalpha():
            word = word[1:]

        while word and not word[-1].isalpha():
            word = word[:-1]
        
        if not word:
            return temp
        return word

    def _baseline_rate(self):
        unseen_words_count = 0.0
        total_test_words = float(sum(self._test_vocab.values()))

        for word in self._test_vocab.keys():
            if word not in self._train_vocab:
                unseen_words_count += 1.0
        
        print("=" * 30)
        print("Baseline OOV rate")
        print(f"Number of unseen words: {unseen_words_count}")
        print(f"Total number of test words: {total_test_words}")
        print(f"OOV rate: {unseen_words_count / total_test_words}")
        print("=" * 30)
