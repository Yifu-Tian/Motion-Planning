import matplotlib.pyplot as plt

def plot_and_show(mean_reward, std_reward, collision_rate, success_rate, episode_rewards):
    
    print(f"Mean Reward: {mean_reward}, Standard Deviation of Reward: {std_reward}")
    print(f"Collision Rate: {collision_rate}, Success Rate: {success_rate}")

    plt.figure(figsize=(10, 4))

    # 累积奖励图表
    plt.subplot(1, 2, 1)
    plt.plot(episode_rewards, marker='o')
    plt.title('Cumulative Reward per Episode')
    plt.xlabel('Episode')
    plt.ylabel('Cumulative Reward')

    # 成功率和碰撞率图表
    plt.subplot(1, 2, 2)
    plt.bar(['Success Rate', 'Collision Rate'], [success_rate, collision_rate], color=['blue', 'red'])
    plt.title('Success and Collision Rates')
    plt.ylabel('Rate')

    plt.tight_layout()
    plt.show()