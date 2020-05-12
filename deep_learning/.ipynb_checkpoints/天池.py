import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
from tqdm import tqdm
import random
from keras.layers import Conv1D, MaxPooling1D, GlobalAveragePooling1D, Dense, Dropout, Input, Embedding, Lambda, LSTM
from keras.models import Model
from keras import backend as K
from sklearn.model_selection import train_test_split
from collections import Counter

multi_class = {}
multi_class2 = {}
with open('/Volumes/xiangch/天池_data/hf_round1_arrythmia.txt', 'r', encoding='utf-8') as r:
    count = 0
    for line in r.readlines():
        count += 1
        multi_class2[count] = line.rstrip()
        multi_class[line.rstrip()] = count

ecg_data = []
# ecg_data_label = []
label_index = {}
with open('/Volumes/xiangch/天池_data/hf_round1_label.txt', 'r', encoding='utf-8') as r:
    for line in r.readlines():
        temp = line.rstrip().split('\t')
        label_index[temp[0]] = [multi_class[i] for i in temp[3:]]
        # ecg_data_label.append([multi_class[i] for i in temp[3:]])
        ecg_data.append(temp[:3])
ecg_basic_info = pd.DataFrame(ecg_data)
# plt.hist(ecg_data_info.iloc[:, 1])

path = '/Volumes/xiangch/天池_data/train'
train_list = os.listdir(path)
ecg_wave_data = []
ecg_data_label = []
x = np.zeros((24106, 5000, 8), dtype=np.int)
i = -1
for doc in tqdm(train_list[:1]):
    i += 1
    for j in range(8):
        x[i, :, j] = pd.read_csv(os.path.join(path, doc), sep=' ', engine='python').iloc[:8000, j].values
    ecg_data_label.append(label_index[doc])

# 多输出标签矩阵化
y = MultiLabelBinarizer().fit_transform(ecg_data_label)



X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2)


# model
batch_size = 64
num_classes = 55
feature_size = 64
epochs = 2

input_data = Input(shape=(5000, 8))
cnn = Conv1D(80, 10, activation='relu')(input_data)
cnn = MaxPooling1D(5)(cnn)
cnn = Dropout(0.3)(cnn)
cnn = Conv1D(80, 10, activation='relu')(cnn)
cnn = MaxPooling1D(5)(cnn)
cnn = Dropout(0.3)(cnn)
cnn = Conv1D(40, 10, activation='relu')(cnn)
cnn = MaxPooling1D(3)(cnn)
cnn = Dropout(0.3)(cnn)
cnn = Conv1D(60, 10, activation='relu')(cnn)
cnn = GlobalAveragePooling1D()(cnn)
cnn = Dropout(0.3)(cnn)
#cnn = Flatten()(cnn)
feature = Dense(feature_size, activation='relu', name='feature')(cnn)
predict = Dense(num_classes, activation='sigmoid', name='sigmoid')(feature) #至此，得到一个常规的so ftmax分类模型

model_trian = Model(inputs=input_data, outputs=predict)
model_trian.compile(optimizer='adam', loss='binary_crossentropy',  metrics=['accuracy'])
#binary_crossentropy
model_trian.summary()

# fit
model_trian.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs,
                 validation_data=[X_test, Y_test])

# predict
model_trian.evaluate(X_test, Y_test)

path = 'E:/项目/hf_round1_testA/testA/'
train_list = os.listdir(path)
ecg_wave_data = []
ecg_data_label = []
x_test = np.zeros((2000, 5000, 8), dtype=np.int)
i = -1
for doc in tqdm(train_list[:2000]):
    i += 1
    for j in range(8):
        x_test[i, :, j] = pd.read_csv(path + doc, sep=' ', engine='python').iloc[:5000, j].values

pred = model_trian.predict(X_test, batch_size=32, verbose=0)

pred = model_trian.predict(x_test, batch_size=32, verbose=0)


pred_bool = ((pred > 0.5) - 1)*2 + 1
results = pd.DataFrame(index=range(1600), columns=range(55))
for i in range(pred_bool.shape[0]):
    for idx in np.where(pred_bool[i, :] == 1)[0]:
        results.iloc[i, idx] = multi_class2[idx + 1]

# 计算测试集上的score
count = 1
for j in range(results.shape[0]):
    if list(results.iloc[j, :][results.iloc[j, :].isnull() == False].index) == list(np.where(Y_test[j, :] == 1)[0]):
        count += 1
print(count/j)