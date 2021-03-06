from collections import Counter
import matplotlib.pyplot as plt

def get_vocab(path):
    with open(path) as f:
        data = f.read()
        vocab = Counter(data.split())
    return vocab


def compute_oov_rate(train_vocab, test_vocab):
    oov_words = list(test_vocab.keys() - train_vocab.keys())
    count_oov = 0
    for k, v in test_vocab.items():
        if k in oov_words:
            count_oov += v

    oov_rate = count_oov / sum(test_vocab.values())
    return oov_rate


def augment_vocab(train_vocab, add_vocab):
    for k, v in add_vocab.items():
        if k not in train_vocab:
            train_vocab.update({k: v})
        else:
            train_vocab.update({k: train_vocab[k] + v})
    return train_vocab


def plot_oov_rates(oov_rates) -> None:
    fig, ax = plt.subplots()
    plt.loglog(list(oov_rates.keys()), list(oov_rates.values()))
    ax.set_xlabel("vocab size")
    ax.set_ylabel("OOV rate")
    plt.legend()
    plt.show()
