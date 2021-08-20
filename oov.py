import os
import json
from copy import deepcopy
from collections import Counter, defaultdict

from nltk.util import pr


class OOV:
    def __init__(self, lang="eng") -> None:
        self._train_path = f"./data/processed/{lang}_train.txt"
        self._test_path = f"./data/processed/{lang}_test.txt"
        self._train_vocab = Counter()
        self._test_vocab = Counter()

        self._init_baseline()
        unseen_words, total_words = self._calc_oov_rate(self._train_vocab)
        self._print_oov_rate("Baseline", unseen_words, total_words)

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

    def _calc_oov_rate(self, train_vocab):
        unseen_words_count = 0.0
        total_test_words = float(sum(self._test_vocab.values()))

        for word in self._test_vocab.keys():
            if word not in train_vocab:
                unseen_words_count += 1.0

        return unseen_words_count, total_test_words

    def _print_oov_rate(self, model, unseen_words, total_words):
        print("=" * 30)
        print(f"{model} OOV rate")
        print(f"Number of unseen words: {unseen_words}")
        print(f"Total number of test words: {total_words}")
        print(f"OOV rate: {unseen_words / total_words}")
        print("=" * 30)

    def check_oov(self):
        gen_dir_path = "./data/generated"
        oov_rates = defaultdict(list)

        for dir in os.listdir(gen_dir_path):
            for i in range(1, 8):
                size = 10**i
                file_path = os.path.join(gen_dir_path, dir, f"{size}_desegmented.txt")
                au_train_vocab = deepcopy(self._train_vocab)

                print(f"{dir}_{size}")

                with open(file_path, 'r') as reader:
                    for line in reader:
                        words = [self._clean_word(word) for word in line.split()]
                        au_train_vocab.update(words)

                unseen_words, total_words = self._calc_oov_rate(au_train_vocab)
                oov_rates[dir].append((size, unseen_words / total_words))

                        #self._print_oov_rate(f"{dir}_{size}", unseen_words, total_words)

        #print(oov_rates)
        with open("dump.json", 'w') as json_writer:
            json.dump(oov_rates, json_writer, indent=4)

                
