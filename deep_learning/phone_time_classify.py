from faker import Faker
import time
import random
import numpy as np
import os
from keras.layers import  MaxPooling1D, GlobalAveragePooling1D, Dense, Dropout, Input, Embedding, Lambda, LSTM
from keras.models import Model
from keras import backend as K
from sklearn.model_selection import train_test_split

f=Faker(locale='zh_CN')

data_num = 10000
time_data = []
id_data = []
phone_data = []
num_data = []

# 时间
time_mark = ['%Y%m%d', '%Y', '%Y%m', '%Y%m%d%H%M%S', '%Y%m%d%I%M%S', '%Y-%m-%d %H:%M:%S',
              '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %I:%M:%S', '%Y/%m/%d %I:%M:%S', '%Y/%m/%d', '%Y/%m',
              '%Y-%m-%d', '%Y-%m']

for i in range(data_num):
    index = int(i % len(time_mark))
    x = time.localtime(f.date_time().timestamp())
    time_data.append(time.strftime(time_mark[index], x))

# 身份证
for i in range(data_num):
    id_data.append(f.ssn())

# 手机
for i in range(data_num):
    phone_data.append(f.phone_number())

# 数字
for i in range(data_num):
    ind = int(i % 18) + 1
    num = ''.join([str(random.randint(0, 9)) for x in range(ind)])
    while num[0] == '0' and len(num) > 2:
        num = num[1:]
    num_data.append(num)

dic = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '0':10,
    ' ':11,
    '/':12,
    '-':13,
    ':':14,
    'X':15
}
data_all = [time_data, id_data, phone_data, num_data]
data = np.zeros([0, 19])
for dd in data_all:
    xx = np.zeros([data_num, 19])
    for i in range(data_num):
        for j, s in enumerate(dd[i]):
            xx[i, j] = dic[s]
    data = np.r_[data, xx]

y = np.array([i for i in range(4) for j in range(data_num)])


x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2, stratify=y)




input_data = Input(shape=(19,))
nn = Dense(32, activation='relu')(input_data)
nn = Dense(64, activation='relu')(nn)
nn = Dense(16, activation='relu')(nn)
predict = Dense(4, activation='softmax', name='softmax')(nn)

model = Model(inputs=input_data, outputs=predict)
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=32, epochs=20,
          validation_data=[x_test, y_test])


####

dic_name = {0: '时间', 1: '身份', 2: '号码', 3: '数字'}

x = str(input())
x=  '15757127314'
xx = np.zeros(19)
for i, s in enumerate(x):
    xx[i] = dic[s]
y = model.predict(xx.reshape(1, -1))[0]
ind = np.argmax(y)
print(dic_name[ind])