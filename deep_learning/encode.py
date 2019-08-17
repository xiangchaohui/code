import numpy as np
import os
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Input, Reshape, UpSampling2D, GlobalAveragePooling2D
from keras.models import Model
from keras.layers.core import Flatten
from sklearn.model_selection import train_test_split
import random
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

data = load_digits()
x = data['data'] # data['images']
y = data['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y)


# input = Input(shape=(64, 64, 1))
# cnn = Conv2D(32, (3, 3), activation='relu')(input)
# cnn = Conv2D(64, (3, 3), activation='relu')(cnn)
# cnn = MaxPooling2D(3, 3)(cnn)
# encode = GlobalAveragePooling2D()(cnn)
#
#
# Encode = Model(inputs=input, outputs=encode)
# Decode = Model(inputs=input, outputs=decode)
#
#
# Decode.compile(optimizer='adam', loss='mse')
# history = Decode.fit(train_data, train_data,
#            batch_size=32, epochs=50,
#            validation_data=[test_data, test_data])

input = Input(shape=(64,))
nn = Dense(128, activation='relu')(input)
encode = Dense(64)(nn)
nn = Dense(128, activation='relu')(encode)
decode = Dense(64)(nn)

Encode = Model(inputs=input, outputs=encode)
Decode = Model(inputs=input, outputs=decode)

Decode.compile(optimizer='adam', loss='mse')
history = Decode.fit(x_train, x_train,
           batch_size=32, epochs=50,
           validation_data=[x_test, x_test])


input = Input(shape=(64,))
nn = Dense(128, activation='relu')(input)
decode = Dense(64)(nn)
ddd= Model(inputs=input, outputs=decode)

ddd.compile(optimizer='adam', loss='mse')
history = ddd.fit(Decode.predict(x_train), x_train,
           batch_size=32, epochs=50,
           validation_data=[x_test, x_test])

plt.figure()
num = random.randint(0, len(x_train))
re = x_train[num, :].reshape(1, -1)
en = Encode.predict(re)
de = ddd.predict(en)

plt.subplot(131)
plt.imshow(re.reshape(8, 8), cmap='gray')
plt.subplot(132)
plt.imshow(en.reshape(8, 8), cmap='gray')
plt.subplot(133)
plt.imshow(de.reshape(8, 8), cmap='gray')

plt.figure()
plt.plot(re[0, :])
plt.plot(en[0, :])
plt.plot(de[0, :])


aa = np.array([random.randint(0, 16) for i in range(64)]).reshape(1, -1)
de = ddd.predict(aa)
plt.subplot(121)
plt.imshow(aa.reshape(8, 8), cmap='gray')
plt.subplot(122)
plt.imshow(de.reshape(8, 8), cmap='gray')
