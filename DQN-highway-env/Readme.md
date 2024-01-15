## 基于Deep Q-Network算法和highway-env仿真环境的车道变更策略

### Intro
DQN算法是强化学习算法中的一个入门级别的算法，stable-baselines3库中已经集成了，因此可以“拿来主义”，不需要太多相关的算法推导细节就能上手使用。当然了解算法的核心思想一定是重中之重。

强化学习中的策略可以按照目标策略和行为策略进行分类:
- 目标策略 target policy: 智能体要学习的策略
- 行为策略 behavior policy: 智能体与环境交互的策略, 即用于生成行为的策略

Q-learning 是一种off-policy TD方法. 所谓off-policy就是指行为策略和目标策略不是同一个策略, 智能体可以通过离线学习自己或别人的策略来指导自己的行为; 与之相反, on-policy的行为策略和目标策略是同一个策略。

Q-learning算法: 该算法中存在一张表格, 记录每个状态下执行每个动作所得到的Q值, 在选取动作时会进行表格的查阅, 然后选取Q值最大的动作

DQN算法: 当状态和动作为连续的, 无限的, 通过表格的方式记录就不合理了, 采用神经网络来替代表格, 输入为状态, 输出为动作。 DQN原始论文：[Playing Atari with Deep Reinforcement Learning](https://arxiv.org/pdf/1312.5602.pdf)

### highway-env
在用Carla进行仿真之前, 我打算先用highway-env简单上手一下RL, 了解到一个自动驾驶模拟环境[highway-env](https://github.com/Farama-Foundation/HighwayEnv), 由Edouard Leurent开发和维护, 其中包含6个场景
- 高速公路"highway-v0"
- 汇入"merge-v0"
- 环岛"parking-v0"
- 十字路口"intersection-v0"
- 赛车道"racetrack-v0"
[官方文档](https://highway-env.farama.org/)

总共分为四个步骤，具体细节和问题记录在Research_Progress.pdf中
- 安装环境
- 配置环境
- 训练模型
- 总结
### HOW TO EXECUTE
1. 在train_model.py中修改参数，训练模型，模型文件会自动生成并保存为highway_dpn_model.zip
2. 在main.py中修改模型文件路径，测试模型性能，输出demo，mean_reward，collision_rate和success_rate图像

### Reference
[stable-baseline3](https://stable-baselines3.readthedocs.io/en/master/modules/dqn.html)  
[基于DQN强化学习的高速路决策控制 - Colin.Fang的文章 - 知乎](
https://zhuanlan.zhihu.com/p/591065890)  
[基于PPO自定义highway-env场景的车辆换道决策 - Colin.Fang的文章 - 知乎
](https://zhuanlan.zhihu.com/p/616670173)  
[DQN算法实现注意事项及排错方法
](https://zhuanlan.zhihu.com/p/169456820)  
[DQN实现高速超车（复现 deeptraffic:MIT 6.S094: Deep Learning for Self-Driving Cars）](https://blog.csdn.net/drilistbox/article/details/80161234?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-12-80161234-blog-121444571.235^v40^pc_relevant_anti_vip_base&spm=1001.2101.3001.4242.7&utm_relevant_index=15)  
[深度强化学习训练与调参技巧](https://zhuanlan.zhihu.com/p/482656367)  
[Carla教程](https://www.zhihu.com/column/c_1324712096148516864)  
