import numpy as np
from stable_baselines3 import DQN


# 评估模型的函数, 计算累计奖励, 平均奖励, 成功率和碰撞率
def evaluate_model(model, env, n_eval_episodes):

    episode_rewards = []
    collisions = 0
    successes = 0
    
    for episode in range(n_eval_episodes):
        obs = env.reset()
        done = False
        total_rewards = 0
        
        flag = 0
        while not done:
            action, _states = model.predict(obs, deterministic = True)
            obs, reward, done, info = env.step(action)
            total_rewards += reward
            
            # 检查是否碰撞或成功完成任务
            if info[0].get('crashed') == True: 
                collisions += 1
                flag = 1
                # break
        # 只有当整个过程中都不发生碰撞时, 即flag恒为1, 才把successes+1
        if flag == 0: successes += 1
        else: flag = 0
        
        episode_rewards.append(total_rewards)
    
    collision_rate = collisions / n_eval_episodes
    success_rate = successes / n_eval_episodes
    
    return collision_rate, success_rate, episode_rewards
