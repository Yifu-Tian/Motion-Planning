from stable_baselines3 import DQN
from env_setup import create_env
from evaluate_model import evaluate_model
from plot_and_show import plot_and_show
from stable_baselines3.common.evaluation import evaluate_policy
def main():
    
    # re-create environment
    env = create_env()
    
    # load model
    model = DQN.load("C:\\Users\\12247\\Desktop\\Purdue\\DQN\\highway_dqn_model.zip", env=env)
    
    collision_rate, success_rate, episode_rewards = evaluate_model(
    model,
    model.get_env(),
    n_eval_episodes=10)
    
    mean_reward, std_reward = evaluate_policy(
    model,
    model.get_env(),
    deterministic=True,
    render=True,
    n_eval_episodes=10)
    
    env.render()
    
    # plot and print
    plot_and_show(mean_reward, std_reward, collision_rate, success_rate, episode_rewards)

if __name__ == "__main__":
    main()