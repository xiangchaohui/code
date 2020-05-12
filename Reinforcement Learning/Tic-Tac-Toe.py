import random
import numpy as np
import matplotlib.pyplot as plt

class Tabel():
    def __init__(self):
        self.state = np.zeros([3, 3])
        self.step_name = 'abcdefghi'
        self.output_state = 'NNNNNNNNN'
        self.step_save = set([x for x in self.step_name])
        self.step_dict = {}
        for i in range(9):
            self.step_dict[self.step_name[i]] = (i // 3, i % 3)
        self.if_end = False
        self.winner = 0

    def step(self, action, action_name):
        self.step_save.remove(action)
        self.state[self.step_dict[action]] = action_name
        self.trans()
        self.judge()

    def judge(self):
        result = list(np.sum(self.state, axis=0)) + list(np.sum(self.state, axis=1))
        result.extend([sum(self.state[[0, 1, 2], [0, 1, 2]]), sum(self.state[[0, 1, 2], [2, 1, 0]])])
        if np.max(result) == 3:
            self.if_end = True
            self.winner = 1
        elif np.min(result) == -3:
            self.if_end = True
            self.winner = -1
        elif 0 not in self.state:
            self.if_end = True
            self.winner = 0
        else:
            self.if_end = False
            self.winner = 0

    def trans(self):
        output_state = ''
        for i in self.state:
            for j in i:
                if j == -1:
                    output_state = output_state + 'X'
                elif j == 1:
                    output_state = output_state + 'O'
                else:
                    output_state = output_state + 'N'
        self.output_state = output_state


class Player():
    def __init__(self, rate, explore):
        self.policy = {}
        self.explore = explore
        self.now_game = []
        self.tabel = None
        self.first_one = 1
        self.rate = rate

    def think(self, state, step_save):
        action_random = random.sample(step_save, 1)[0]
        if state not in self.policy:
            action = action_random
            self.now_game.append([state, action, False])
            self.policy[state] = dict()
            for name in step_save:
                self.policy[state][name] = [0, 0, 0, 0.5]  # win, lose, draw, value
        else:
            explore = np.random.binomial(1, self.explore)
            action_list = []
            win_list = []
            for name in self.policy[state]:
                action_list.append(name)
                win_list.append(self.policy[state][name][3])
            max_win_index = int(np.argmax(win_list))
            action_policy = action_list[max_win_index]
            if explore == 1:
                action = action_random
                self.now_game.append([state, action, False])
            else:
                action = action_policy
                self.now_game.append([state, action, True])
        return action

    def action(self):

        output_state = self.trange_()
        action = self.think(output_state, self.tabel.step_save)
        self.tabel.step(action, self.first_one)

    def backup(self):
        step = self.now_game[-1]
        self.policy[step[0]][step[1]][2] += 1
        self.policy[step[0]][step[1]][self.first_one * self.tabel.winner != 1] += 1
        self.policy[step[0]][step[1]][3] = self.first_one * self.tabel.winner
        step_all = self.now_game[::-1]
        for i, step in enumerate(step_all[1:]):
            self.policy[step[0]][step[1]][2] += 1
            self.policy[step[0]][step[1]][self.first_one * self.tabel.winner != 1] += 1
            v_s = self.policy[step[0]][step[1]][3]
            v_s_star = self.policy[step_all[i-1][0]][step_all[i-1][1]][3]
            if_up = step_all[i-1][2]
            v_s_new = v_s + self.rate * (v_s_star - v_s) * if_up
            self.policy[step[0]][step[1]][3] = v_s_new
        self.now_game = []

    def trange_(self):
        if self.first_one:
            return self.tabel.output_state
        else:
            output_state = ''
            for a in self.tabel.output_state:
                if a == 'X':
                    output_state = output_state + 'O'
                elif a == 'O':
                    output_state = output_state + 'X'
                else:
                    output_state = output_state + 'N'
            return output_state


def compete(player1, player2):

    p1 = 0
    p2 = 0
    pp = 0
    result = []
    for i in range(100000):
        tabel = Tabel()
        player1.tabel = tabel
        player2.tabel = tabel
        if random.sample([0, 1], 1)[0] == 1:
            player1.first_one = 1
            player2.first_one = -1

            while True:
                player1.action()
                if tabel.if_end:
                    player1.backup()
                    player2.backup()
                    p1 += tabel.winner
                    pp += tabel.winner == 0
                    break

                player2.action()
                if tabel.if_end:
                    player1.backup()
                    player2.backup()
                    p2 += -tabel.winner
                    pp += tabel.winner == 0
                    break
        else:
            player1.first_one = -1
            player2.first_one = 1

            while True:
                player2.action()
                if tabel.if_end:
                    player1.backup()
                    player2.backup()
                    p2 += tabel.winner
                    pp += tabel.winner == 0
                    break

                player1.action()
                if tabel.if_end:
                    player1.backup()
                    player2.backup()
                    p1 += -tabel.winner
                    pp += tabel.winner == 0
                    break

        if i % 1000 == 0:
            print(i, p1, p2, pp)
        result.append([p1, p2, pp])
    result = np.array(result)
    plt.plot(result[:, 0] / np.sum(result, axis=1))
    plt.show()



######## 开始比赛


player1 = Player(rate=0.1, explore=0.1)
player2 = Player(rate=0.1, explore=0.1)
compete(player1, player2)


####### 人机对战 先手

tabel = Tabel()
player2.first_one = -1
player2.tabel = tabel
while True:

    action = input()
    tabel.step(action, 1)
    print(tabel.state)
    if tabel.if_end and tabel.winner == 1:
        print('you win!')
        break
    if tabel.if_end and tabel.winner == 0:
        print('平局')
        break

    player2.action()
    print(tabel.state)
    if tabel.if_end and tabel.winner == -1:
        print('you lose!')
        break
    if tabel.if_end and tabel.winner == 0:
        print('平局')
        break


####### 人机对战 后手

tabel = Tabel()
player1.first_one = 1
player1.tabel = tabel
while True:

    player1.action()
    print(tabel.state)
    if tabel.if_end and tabel.winner == 1:
        print('you lose!')
        break
    if tabel.if_end and tabel.winner == 0:
        print('平局')
        break

    action = input()
    tabel.step(action, -1)
    print(tabel.state)
    if tabel.if_end and tabel.winner == -1:
        print('you win!')
        break
    if tabel.if_end and tabel.if_end:
        print('平局')
        break

