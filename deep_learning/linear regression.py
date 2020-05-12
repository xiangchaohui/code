import numpy as np
import os
from keras.layers import  Dense, Dropout, Input, Embedding, Lambda, LSTM
from keras.models import Model
from keras import backend as K
from sklearn.model_selection import train_test_split




x = np.arange(-1, 1, 0.02)
y = x * 3 + 0.1 + np.random.normal(0, 0.2, len(x))

input_a = Input(shape=(1,))
out = Dense(1)(input_a)

model = Model(inputs=input_a, outputs=out)

model.compile(optimizer='sgd', loss='mse')

model.fit(x, y, batch_size=10, epochs=100)
plt.scatter(x, y)
plt.plot(x, model.predict(x))



input_a = Input(shape=(1,))
nn = Dense(10, activation='relu')(input_a)
# nn = Dense(3, activation='relu')(nn)
# nn = Dense(3, activation='relu')(nn)
# nn = Dense(3, activation='relu')(nn)
out = Dense(1)(nn)

model = Model(inputs=input_a, outputs=out)

model.compile(optimizer='sgd', loss='mse')

model.fit(x, y, batch_size=10, epochs=100)
plt.scatter(x, y)
plt.plot(x, model.predict(x))