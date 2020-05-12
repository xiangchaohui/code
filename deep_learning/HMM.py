import numpy as np

## 评估--> 给定状态，寻找概率最大的HMM模型
A = np.array([[0.500, 0.375, 0.125],  # 转移矩阵
               [0.250, 0.125, 0.625],
               [0.250, 0.375, 0.375]])
B = np.array([[0.60, 0.20, 0.15, 0.05],  # 隐藏状态到观测状态的概率
               [0.25, 0.25, 0.25, 0.25],
               [0.05, 0.10, 0.35, 0.50]])
M = 4
N = 3
pi = np.array([0.63, 0.17, 0.20])  # 初始状态


T = 3
ot = [1, 3, 4]  # 观测状态


a1 = np.zeros(3)
for i in range(N):
    a1[i] = pi[i] * B[i, ot[0] - 1]

a2 = np.zeros(3)
for i in range(N):
    a2[i] = np.sum(a1 * A[:, i]) * B[i, ot[1] - 1]

a3 = np.zeros(3)
for i in range(N):
    a3[i] = np.sum(a2 * A[:, i]) * B[i, ot[2] - 1]

np.sum(a3) # 观测状态来自该模型的概率


## 寻找最佳隐藏状态

A = np.array([[0.333, 0.333, 0.333],  # 隐藏状态转移矩阵
     [0.333, 0.333, 0.333],
     [0.333, 0.333, 0.333]])

B = np.array([[0.5, 0.5],  # 隐藏状态到观测状态矩阵
     [0.75, 0.25],
     [0.25, 0.75]])

M = 2 # 观测状态数
N = 3 # 隐藏状态数

pi = np.array([0.333, 0.333, 0.333]) # 初始状态

T = 10
ot = [1, 1, 1, 1, 2, 1, 2, 2, 2, 2] # 观测状态


def rou(A, B, pi, ot, ro):
    # TODO 每部计算返回概率
    len_t = len(ot)
    if len_t == 1:
        return pi * B[:, ot[0] - 1], ro
    dat, dro = rou(A, B, pi, ot[:-1], ro)

    at0 = []
    ro0 = [[], [], []]
    for i in range(N):
        s = dat * A[:, i] * B[i, ot[-1] - 1]
        ind = int(np.argmax(s))
        ro0[i] = dro[ind] + [ind + 1]
        at0.append(s[ind])
    return np.array(at0), ro0


rou(A, B, pi, ot, [[], [], []])