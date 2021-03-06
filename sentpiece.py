from os import WIFSTOPPED, write
import sentencepiece as spm


def train_model(data_path, model_prefix, voc_size, lang="eng"):
    if lang == "eng":
        spm.SentencePieceTrainer.train(input=data_path,
                                       model_prefix=model_prefix,
                                       vocab_size=voc_size,
                                       character_coverage=1.0,
                                       model_type="bpe")
    else:
        spm.SentencePieceTrainer.train(input=data_path,
                                       model_prefix=model_prefix,
                                       vocab_size=voc_size,
                                       character_coverage=0.995,
                                       model_type="bpe")


def segmentation(data_path, model_prefix, out_file):
    sp = spm.SentencePieceProcessor(model_file=f"spm_models/{model_prefix}.model")

    with open(data_path, 'r') as reader:
        corpus = reader.read()

    segmented = sp.encode(corpus, out_type=str)

    with open(f"data/segmented/{out_file}", 'w') as writer:
        writer.write(" ".join(segmented))


def desegmentation(data_path, model_prefix):
    sp = spm.SentencePieceProcessor(model_file=f"spm_models/{model_prefix}.model")

    with open(data_path, 'r') as reader:
        corpus = reader.read()

    desegmented = sp.decode(corpus.split(' '))

    data_path = data_path.split(".")
    data_path = "".join([data_path[0], "_desegmented.", data_path[1]])
    
    with open(data_path, 'w') as writer:
        writer.write(desegmented)

def show_desegmented_file(file_path):
    print(file_path[file_path.find("data/generated/")+len("data/generated/"):file_path.rfind("/")])
    with open(file_path) as f:
        print(f.read())
