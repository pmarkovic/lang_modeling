from os import read
import sentencepiece as spm


def train_model(data_path, model_prefix, voc_size):
    spm.SentencePieceTrainer.train(input=data_path, 
                                   model_prefix=model_prefix,   
                                   vocab_size=voc_size, 
                                   character_coverage=1.0, 
                                   model_type="bpe")


def segmentation(data_path, model_prefix, out_file):
    sp = spm.SentencePieceProcessor(model_file=f"spm_models/{model_prefix}.model")

    with open(data_path, 'r') as reader:
        corpus = reader.read()

    segmented = sp.encode(corpus, out_type=str)

    with open(f"data/segmented/{out_file}", 'w') as writer:
        writer.write(" ".join(segmented))

