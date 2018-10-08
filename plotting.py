import matplotlib.pyplot as plt


def plot_arm_probs(num_sims, horizon, choices, n_arms):
    arm_probs = [[0] * horizon for _ in range(n_arms)]
    for arm in range(n_arms):
        for i in range(horizon):
            picked = 0.00
            for j in range(num_sims):
                index = i + j * horizon
                if choices[index] == arm:
                    picked += 1.0
            arm_probs[arm][i] = picked / num_sims

    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('Set1')
    num = 0
    x = range(horizon)
    for arm in range(n_arms):
        num += 1
        plt.plot(x, arm_probs[arm], marker='', \
                              color=palette(num), linewidth=1, alpha=0.9, label=str(arm))
    plt.legend()
    plt.title("Plot of the average probabilities of choosing each arm over time", \
              loc='center', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Time")
    plt.ylabel("Probability")
    plt.show()

def plot_average_rewards(num_sims, horizon, rewards):
    avg_rewards = []
    for h in range(horizon):
        total_reward = 0.0
        for sim in range(num_sims):
            total_reward += rewards[h + horizon * sim]
        avg_rewards.append(float(total_reward)/num_sims)
    plt.style.use('seaborn-darkgrid')
    x = range(horizon)
    plt.plot(x, avg_rewards, marker='', linewidth=1, alpha=0.9)
    plt.title(f"Plot of average rewards at each time step over {num_sims} simulations", \
              loc='center', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Time")
    plt.ylabel("Average Reward")
    plt.show()

def plot_cumulative_rewards(num_sims, horizon, cumulative_rewards):
    avg_cumulative_rewards = []
    for h in range(horizon):
        total_cumulative_reward = 0.0
        for sim in range(num_sims):
            total_cumulative_reward += cumulative_rewards[h + horizon * sim]
        avg_cumulative_rewards.append(float(total_cumulative_reward)/num_sims)
    plt.style.use('seaborn-darkgrid')
    x = range(horizon)
    plt.plot(x, avg_cumulative_rewards, marker='', linewidth=1, alpha=0.9)
    plt.title(f"Plot of average cumulative rewards at each time step over {num_sims} simulations", \
              loc='center', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Time")
    plt.ylabel("Average Cumulative Reward")
    plt.show()
