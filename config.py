# -*- coding: utf-8 -*-
__author__ = 'klb3713'


# Not actually used directly, just for convenience

DATA_DIR = "/home/klb3713/workspace/cw_word_embedding/data/"

## 32-bit for the GPU
##import theano.config as config
##floatX = config.floatX
#floatX = 'float32'

TRAIN_FILE = DATA_DIR + "text8"

SAMPLE_FILE = DATA_DIR + "samples"

# Should we induce an embedding for OOV words?
INCLUDE_UNKNOWN_WORD = True
UNKNOWN_WORD = "*UNKNOWN*"
SYMBOL_WORD = "*SYMBOL*"

VOCABULARY_SIZE = 268810
VOCABULARY_FILE = DATA_DIR + "vocabulary.pkl"

# Use the log-bilinear model or not?
# If True, we predict the Mnih log-bilinear model
# If False, we predict the C&W language model.
LOG_BILINEAR_MODEL = False

# Number of examples per minibach
MINIBATCH_SIZE = 100

# Randomly initialize embeddings uniformly in the range [-this value, +this value]
INITIAL_EMBEDDING_RANGE = 0.01

# l1 penalty appliedto C&W embeddings
CW_EMBEDDING_L1_PENALTY = 0.

NORMALIZE_EMBEDDINGS = False
#UPDATES_PER_NORMALIZE_EMBEDDINGS = 1000

# Number of validation examples
VALIDATION_EXAMPLES = 1000

# What percent of noise examples should we use for computing the logrank
# during validation?
# This is a speed optimization.
PERCENT_OF_NOISE_EXAMPLES_FOR_VALIDATION_LOGRANK = 0.01

NGRAM_FOR_TRAINING_NOISE = 0

#NGRAMS = {(1, 5000) = join(DATA_DIR, "1grams-wikitext-5000.json.gz"),
#(1, 10000) = join(DATA_DIR, "1grams-wikitext-10000.json.gz"),
#(1, 20000) = join(DATA_DIR, "1grams-wikitext-20000.json.gz")}

# Number of instances of each ngram to add, for smoothing.
TRAINING_NOISE_SMOOTHING_ADDITION = 0

# Each embedded word representation has this width
EMBEDDING_SIZE = 50

# Predict with a window of five words at a time
WINDOW_SIZE = 5

HIDDEN_SIZE = 100

# = Scaling value to control range for weight initialization
#SCALE_INITIAL_WEIGHTS_BY = math.sqrt(3)
SCALE_INITIAL_WEIGHTS_BY = 1

# Which activation function to use?
#ACTIVATION_FUNCTION="sigmoid"
#ACTIVATION_FUNCTION="tanh"
ACTIVATION_FUNCTION = "softsign"

LEARNING_RATE = 0.000000011

# The learning rate for the embeddings
EMBEDDING_LEARNING_RATE = 0.00000000034

## number of (higher-order) quadratic filters for James's neuron
#NUMBER_OF_QUADRATIC_FILTERS=0
## We use this scaling factor for initial weights of quadratic filters,
## instead of SCALE_INITIAL_WEIGHTS_BY
## @note = Try between 10 and 0.01
#SCALE_QUADRATIC_INITIAL_WEIGHTS_BY = 1

# Validate after this many examples
VALIDATE_EVERY = 10000000