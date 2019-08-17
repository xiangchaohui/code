from PIL import Image

from pylab import *

import numpy as np

import random


def read_data():
    m1 = np.load('/Users/chaohuixiang/Desktop/Gait_data/视频及手机特征/mobile_feature0.npy')
    m2 = np.load('/Users/chaohuixiang/Desktop/Gait_data/视频及手机特征/mobile_feature.npy')

    v1 = np.load('/Users/chaohuixiang/Desktop/Gait_data/视频及手机特征/video_feature0.npy', allow_pickle=True).item()
    v2 = np.load('/Users/chaohuixiang/Desktop/Gait_data/视频及手机特征/video_feature.npy', allow_pickle=True).item()

    data_m = np.r_[m1, m2]
    data_v = np.zeros([0, 96])
    label_v = []

    for name in v1:
        ss = name.split('_')
        if ss[3] != '1':
            continue
        if ss[4] not in set(['1', '2', '3']):
            continue
        data_v = np.r_[data_v, v1[name].reshape(1, -1)]
        label_v.append(int(ss[0]))

    for name in v2:
        ss = name.split('_')
        if ss[3] != '1':
            continue
        if ss[4] not in set(['1', '2', '3']):
            continue
        data_v = np.r_[data_v, v2[name].reshape(1, -1)]
        label_v.append(int(ss[0]))

    data_v = np.c_[data_v, np.array(label_v).reshape(-1, 1)]

    return data_m, data_v


def make_data(data_m, data_v):
    user_set = set(data_m[:, -1])
    user_dic = {}
    for i, name in enumerate(user_set):
        user_dic[name] = i

    center_data = np.zeros([len(user_set), 129])
    for i, name in enumerate(user_set):
        index = np.where(data_m[:, -1] == name)[0]
        center_data[i, :-1] = np.mean(data_m[index, :-1], axis=0)
        center_data[i, -1] = name

    tr_m = []
    tr_v = []
    tr_user = []
    te_m = []
    te_v = []
    te_user = []

    for i, user in enumerate(user_set):
        ind1 = np.where(data_m[:, -1] == user)[0]
        ind2 = np.where(data_v[:, -1] == user)[0]
        indc = np.where(center_data[:, -1] == user)[0]
        if i < 50:
            tr_user = tr_user + list(indc)
        else:
            te_user = te_user + list(indc)
        for m in random.sample(list(ind1), int(len(ind1)/4)):
            for v in random.sample(list(ind2), int(len(ind2)/4)):
                if i < 50:
                    tr_m.append(m)
                    tr_v.append(v)
                else:
                    te_m.append(m)
                    te_v.append(v)
    tr_m = data_m[np.array(tr_m), :]
    tr_v = data_v[np.array(tr_v), :]
    te_m = data_m[np.array(te_m), :]
    te_v = data_v[np.array(te_v), :]
    tr_c = center_data[np.array(tr_user), :]
    te_c = center_data[np.array(te_user), :]
    print(tr_m.shape, te_m.shape, tr_c.shape)
    return tr_m, tr_v, tr_c, te_m, te_v, te_c


def layerout(w,b,x):
    y = np.dot(w,x) + b
    t = -1.0*y
    # n = len(y)
    # for i in range(n):
        # y[i]=1.0/(1+exp(-y[i]))
    y = 1.0/(1+exp(t))
    return y


def mytrain(tr_m, tr_v, tr_c, te_m, te_v, te_c, epochs=10, rate=0.01, hid=64, batch_size=32):
    '''
    设置一个隐藏层，784-->隐藏层神经元个数-->10
    '''
    n = tr_v.shape[0]
    n_c = len(tr_c)
    step = epochs
    a = rate
    inn = tr_v.shape[1] - 1
    hid = hid
    out = tr_m.shape[1] - 1

    w = np.random.randn(out,hid)
    w = np.mat(w)
    b = np.mat(np.random.randn(out,1)) 
    w_h = np.random.randn(hid,inn)
    w_h = np.mat(w_h)
    b_h = np.mat(np.random.randn(hid,1)) 

    for i in range(step):
        #打乱训练样本
        r=np.random.permutation(n)
        tr_v = tr_v[r,:]
        tr_m = tr_m[r,:]
        #mini_batch
        for j in range(int(n/batch_size)):
            #取batch为10  更新取10次的平均值
            outw_update = 0
            outb_update = 0
            hidw_update = 0
            hidb_update = 0
            for k in range(batch_size):
                x = tr_v[j*batch_size+k,:-1].reshape(-1, 1)
                y = tr_m[j*batch_size+k,:-1]

                hid_put = layerout(w_h,b_h,x)
                out_put = layerout(w,b,hid_put)

                dis_v = np.sum((tr_c[:, :-1] - np.array(out_put).reshape(1, -1)) ** 2, axis=1)
                dis_m = np.sum((tr_c[:, :-1] - y) ** 2, axis=1)

                ind_v = np.argsort(np.argsort(dis_v))
                ind_m = np.argsort(np.argsort(dis_m))

                for p in range(len(ind_v)):
                    yy = tr_c[p, :-1].reshape(-1, 1)
                    button = (ind_v[p] - ind_m[p]) / n_c

                    o_update = np.multiply(np.multiply((yy-out_put),out_put),(1-out_put))
                    h_update = np.multiply(np.multiply(np.dot((w.T),np.mat(o_update)),hid_put),(1-hid_put))

                    outw_update = outw_update + button*a*np.dot(o_update,(hid_put.T))
                    outb_update = outb_update + button*a*o_update
                    hidw_update = hidw_update + button*a*np.dot(h_update,(x.T))
                    hidb_update = hidb_update + button*a*h_update

            w = w + outw_update / batch_size
            b = b + outb_update / batch_size
            w_h = w_h + hidw_update / batch_size
            b_h = b_h + hidb_update / batch_size
        print('Epochs', i, '________________________________')
        mytest(te_m, te_v, te_c, w, b, w_h, b_h)
        mytest(tr_m, tr_v, tr_c, w, b, w_h, b_h)

    return w,b,w_h,b_h


def mytest(te_m, te_v, te_c ,w, b, w_h, b_h):
    '''
    统计1000个测试样本中有多少个预测正确了
    预测结果表示：10*1的列向量中最大的那个数的索引+1就是预测结果了
    '''
    te_m = te_c
    n = te_v.shape[0]

    hid = layerout(w_h,b_h,te_v[:, :-1].transpose())
    pre = layerout(w,b,hid).transpose()

    zz1 = 0
    zz3 = 0
    zz5 = 0

    for i in range(n):
        dis = np.sum((te_m[:, :-1] - np.array(pre[i, :]).reshape(1, -1)) ** 2, axis=1)
        ind = np.argsort(dis)
        if te_v[i, -1] == te_m[ind[0], -1]:
            zz1 += 1
        if te_v[i, -1] in [te_m[k, -1] for k in ind[:3]]:
            zz3 += 1
        if te_v[i, -1] in [te_m[k, -1] for k in ind[:5]]:
            zz5 += 1

    print(np.around(np.array([zz1, zz3, zz5])/n, 3))


data_m, data_v = read_data()
tr_m, tr_v, tr_c, te_m, te_v, te_c = make_data(data_m, data_v)

w, b, w_h, b_h = mytrain(tr_m, tr_v, tr_c, te_m, te_v, te_c, epochs=50, rate=0.1, hid=64, batch_size=32)

dic = {'w': w, 'b': b, 'w_b': w_h, 'b_h': b_h}
np.save('/Users/chaohuixiang/Desktop/Gait_data/视频及手机特征/model.npy', dic)

# Epochs 49 ________________________________
# [0.025 0.025 0.066]
# [0.464 0.464 0.612]