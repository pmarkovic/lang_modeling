import argparse
import nltk
from nltk import parse

from preprocessor import Preprocessor
from sentpiece import train_model, segmentation


if __name__ == "__main__":
    nltk.download("punkt")

    parser = argparse.ArgumentParser(description="Test file!")
    parser.add_argument("-corpath", default="data/eng_train.txt", type=str, help="Path to corpus directory.")
    parser.add_argument("-lang", default="eng", type=str, help="Language of the corpus.")
    parser.add_argument("-m_prefix", default="pmodel", help="Prefix of the model.")
    parser.add_argument("-voc_size", default=1000, help="Size of model vocabulary.")
    parser.add_argument("-seg_file", default="en_s1.txt", type=str, help="File for segmented text.")
    args = parser.parse_args()

    #preprocessor = Preprocessor(args.corpath, args.lang)
    #cleaned_corpus = preprocessor.process()
    #preprocessor.split(cleaned_corpus)

    #train_model(args.corpath, args.m_prefix, args.voc_size)
    segmentation(args.corpath, args.m_prefix, args.seg_file)


