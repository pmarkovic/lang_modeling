import argparse
import nltk

from preprocessor import Preprocessor


if __name__ == "__main__":
    nltk.download("punkt")

    parser = argparse.ArgumentParser(description="Test file!")
    parser.add_argument("-corpath", default="data/alice_in_wonderland.txt", type=str, help="Path to corpus directory.")
    parser.add_argument("-lang", default="eng", type=str, help="Language of the corpus.")
    args = parser.parse_args()

    preprocessor = Preprocessor(args.corpath, args.lang)
    cleaned_corpus = preprocessor.process()
    preprocessor.split(cleaned_corpus)
