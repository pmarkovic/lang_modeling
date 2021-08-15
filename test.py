import argparse

from oov import OOV


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test file!")
    parser.add_argument("-corpath", default="data/eng_train.txt", type=str, help="Path to corpus directory.")
    parser.add_argument("-lang", default="eng", type=str, help="Language of the corpus.")
    parser.add_argument("-m_prefix", default="pmodel", help="Prefix of the model.")
    parser.add_argument("-voc_size", default=1000, help="Size of model vocabulary.")
    parser.add_argument("-seg_file", default="en_s1.txt", type=str, help="File for segmented text.")
    args = parser.parse_args()

    comparer = OOV()

