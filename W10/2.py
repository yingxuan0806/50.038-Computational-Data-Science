# Import necessary libraries

import sys
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# Load in dataset of sample text and some preprocessing (convert to lowercase)

filename = "shakespeare.txt"
text = open(filename).readlines()[:4000]
text = ''.join(text)
text = text.lower()

# Fuctions for mapping characters to integers and vice versa. Our text generation task will generate character-by-character.

chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate(chars)) # convert characters to integers
int_to_char = dict((i, c) for i, c in enumerate(chars)) # convert integers to characters
doc_size = len(text)
vocab_size = len(chars)

# Prepare dataset and labels for our training process, where we use sequences of 50 characters to generate the 51st character. Keras requries input to be in the shape [samples, time steps, features].

seq_length = 50
x_train = []
y_train = []
for i in range(0, doc_size - seq_length, 1):
	seq_in = text[i:i + seq_length]
	seq_out = text[i + seq_length]
	x_train.append([char_to_int[char] for char in seq_in])
	y_train.append(char_to_int[seq_out])
seq_size = len(x_train)
y_train = np_utils.to_categorical(y_train) # convert to one-hot
x_train = np.reshape(x_train, (seq_size, seq_length, 1)) # reshape and normalize values

# Construct and train our LSTM model

model = Sequential()
model.add(LSTM(256, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(Dense(y_train.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x_train, y_train, epochs=20, batch_size=3000)

# Generate a new text based on provided seed text
seed_text = "out of grief and impatience. answer'd neglectingly"
pattern = [char_to_int[char] for char in seed_text]
print(len(pattern))
# generate characters
generated_text = ""
x = np.reshape(pattern, (1, len(pattern), 1))
print(x.shape)
prediction = model.predict(x, verbose=0)
index = np.argmax(prediction)
result = int_to_char[index]
generated_text+=result
print("Generated Text:")
print(generated_text)