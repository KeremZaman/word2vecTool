# word2vecTool
A useful tool for preprocessing text  and creating word vectors from it.


#Install Dependencies
This tool uses gensim to create word2vec. It can be installed using pip:
'''
pip install gensim
'''

#Usage
'''
usage: x.py [-h] --input INPUT [--model MODEL] [--workers WORKERS]
            [--size SIZE] [--only-preprocess ONLY_PREPROCESS]
            [--only-train ONLY_TRAIN]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         Input to generate vectors (raw file for default,
                        preprocessed file for only-train mode ) (default:
                        None)
  --model MODEL         Name for model (default: model)
  --workers WORKERS     Workers for training (default:4) (default: 4)
  --size SIZE           Dimension of vectors (default:300) (default: 300)
  --only-preprocess ONLY_PREPROCESS
                        Only preprocess input file, enter name for output
                        (default: None)
  --only-train ONLY_TRAIN
                        Only train preprocessed input file, enter name for
                        output (default: None)
'''
