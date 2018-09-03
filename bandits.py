import random
from abc import ABCMeta, abstractmethod
import math


class BanditAlgorithm():
    def __init__(self, n_arms):
        self.n_arms = n_arms
        self.counts = []
        self.values = []
        self.reset_stats()

    def reset_stats(self):
        self.counts = [0 for _ in range(self.n_arms)]
        self.values = [0.0 for _ in range(self.n_arms)]

    @abstractmethod
    def select_arm(self):
        pass

    @abstractmethod
    def update(self, arm, reward):
        pass


class EpsilonGreedy(BanditAlgorithm):

    def __init__(self, epsilon, n_arms):
        super().__init__(n_arms)
        self.epsilon = epsilon

    def select_arm(self):
        if random.random() > self.epsilon:
            return self.__find_best_arm()
        return random.randrange(self.n_arms)

    def __find_best_arm(self):
        m = max(self.values)
        return self.values.index(m)

    def update(self, arm, reward):
        self.counts[arm] += 1
        c = self.counts[arm]
        self.values[arm] = ((self.values[arm] * (c - 1)) + reward) / float(c)

class Softmax(BanditAlgorithm):

    def __init__(self, n_arms, temperature):
        super().__init__(n_arms)
        self.temperature = temperature

    def __categorical_draw(self, probs):
        z = random.random()
        cum_prob = 0.0
        for i in range(len(probs)):
            prob = prob[i]
            cum_prob += prob
            if cum_prob > z:
                return i
        return len(probs) - 1

    def select_arm(self):
        z = sum([math.exp(v / self.temperature) for v in self.values])
        probs = [math.exp(v / self.temperature) / z  for v in self.values]
        return self.__categorical_draw(probs)

    def update(self, arm, reward):
        self.counts[arm] += 1
        c = self.counts[arm]
        self.values[arm] = ((self.values[arm] * (c - 1)) + reward) / float(c)









