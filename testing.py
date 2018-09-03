import random

class BernoulliArm():
    def __init__(self, p):
        self.p = p

    def draw(self):
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0

def test_algorithm(algo, arms, num_sims, horizon):
    chosen_arms = [0.0 for _ in range(num_sims * horizon)]
    rewards = [0.0 for _ in range(num_sims * horizon)]
    cumulative_rewards = [0.0 for _ in range(num_sims * horizon)]
    sim_nums = [0.0 for _ in range(num_sims * horizon)]
    times = [0.0 for _ in range(num_sims * horizon)]

    for sim in range(num_sims):
        sim += 1
        algo.reset_stats()
        for t in range(horizon):
            t += 1
            index = (sim - 1) * horizon + t - 1
            sim_nums[index] = sim
            times[index] = t
            chosen_arm = algo.select_arm()
            chosen_arms[index] = chosen_arm
            reward = arms[chosen_arms[index]].draw()
            rewards[index] = reward
            if t == 1:
                cumulative_rewards[index] = reward
            else:
                cumulative_rewards[index] = cumulative_rewards[index - 1] + reward
            algo.update(chosen_arm, reward)

    return [sim_nums, times, chosen_arms, rewards, cumulative_rewards]
