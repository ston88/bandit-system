import random
from testing import BernoulliArm
from bandits import EpsilonGreedy, Softmax
from testing import test_algorithm
from plotting import plot_arm_probs, plot_average_rewards, plot_cumulative_rewards


def main():
    random.seed(1)
    means = [0.1] * 4 + [0.9]
    n_arms = len(means)
    random.shuffle(means)
    arms = list(map(lambda x: BernoulliArm(x), means))
    print('Best arm is:', means.index(max(means)))
    num_sims = 5000
    horizon = 500
    l = list(map(lambda x: x * 0.1, range(1, 6)))
    for t in l:
        algo = Softmax(temperature=t, n_arms=n_arms)
        res = test_algorithm(algo, arms, num_sims=num_sims, horizon=horizon)
        cumulative_rewards = res[4]
        rewards = res[3]
        plot_cumulative_rewards(num_sims=num_sims, horizon=horizon, cumulative_rewards=cumulative_rewards)
        plot_average_rewards(num_sims=num_sims, horizon=horizon, rewards=rewards)
        plot_arm_probs(num_sims=num_sims, horizon=horizon, choices=res[2], n_arms=n_arms)


if __name__ == '__main__':
    main()