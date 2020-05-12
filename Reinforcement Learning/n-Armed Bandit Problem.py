import numpy as np
import matplotlib.pyplot as plt

true_q = np.random.normal(0, 1, 10) + 1


def test(n=2000, e=1):
    estimated_value = np.zeros(10)
    value_all_mean = []

    for i in range(n):
        action = np.zeros([2000])
        action_random_num = np.random.binomial(2000, e)
        action_best_num = 2000 - action_random_num

        action[:action_random_num] = np.random.randint(0, 10, action_random_num)
        action[action_random_num:] = np.argmax(estimated_value)

        noise = np.random.normal(0, 1, 2000)
        value_all_mean.append((np.sum(true_q[action.astype(np.int64)]) + np.sum(noise)) / 2000)

        for aa in range(10):
            index = np.where(action == aa)[0]
            if len(index) == 0:
                continue
            estimated_value[aa] = np.mean(true_q[action[index].astype(np.int64)] + noise[index])

    return estimated_value, value_all_mean


# ε-greedy methods
def test2(n=1000, e=1):
    vm = np.zeros(1000)
    for example in range(2000):
        estimated_value = np.zeros(10)
        value_all = []
        value_all_mean = []
        value_dict = {}
        for i in range(10):
            value_dict[i] = []

        for i in range(n):

            if np.random.binomial(1, e):
                action = np.random.randint(0, 10, 1)[0]
            else:
                action = np.argmax(estimated_value)

            value = true_q[action] + np.random.normal(0, 1, 1)[0]
            value_all.append(value)
            value_all_mean.append(np.mean(value_all))
            value_dict[action].append(value)
            estimated_value[action] = np.mean(value_dict[action])
        vm = vm + np.array(value_all_mean)
    vm = vm / 2000
    return estimated_value, vm

import time
t1 = time.time()
estimated_value0, mean_value0 = test2(n=1000, e=0)
estimated_value1, mean_value1 = test2(n=1000, e=0.1)
estimated_value2, mean_value2 = test2(n=1000, e=0.01)
print(time.time()-t1)
plt.plot(mean_value0, label='0')
plt.plot(mean_value1, label='0.1')
plt.plot(mean_value2, label='0.01')
plt.legend()