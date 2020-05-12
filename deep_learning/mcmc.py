import numpy as np
import matplotlib.pyplot as plt
import random
from collections import Counter

ma = [[12,53,41,4,6],
     [12,21,52,13,5],
     [65,32,24,16,8],
     [32,34,52,31,12],
     [44,33,25,14,15]]
ma = np.array(ma)
mb = np.zeros([5,5])
for i in range(5):
    a = ma[i, :].copy()
    b = np.array(a / np.sum(a))
    mb[i, :] = b
ma = mb


result = np.zeros([100, 5])
a = [1,13,52,12,23]
a = a / np.sum(a)
result[0, :] = a

for i in range(1, 100):
    result[i, :] = np.matmul(result[i-1, :].reshape([1, num]), ma)[0, :]


for i in range(5):
    plt.plot(result[:, i], label=str(i))
plt.legend()


star_pi = result[-1, :]
data = []
for i in range(5):
    aa = []
    for j in range(5):
        aa.extend([j for num in range(int(10000000*ma[i, j]))])
    data.append(aa)
plot_data = []
x = 0
for i in range(100000):
    x = random.sample(data[x], 1)[0]
    plot_data.append(x)

a = Counter(plot_data)
b = [a[i]/100000 for i in range(5)]

plt.scatter(range(5), b)
plt.scatter(range(5), result[-1, :])