from stable_baselines3 import DQN
from env_setup import create_env

model = DQN('MlpPolicy',
        create_env(),
        policy_kwargs=dict(net_arch=[256, 256]),
        learning_rate=5e-4,
        buffer_size=15000,
        learning_starts=200,
        batch_size=32,
        gamma=0.8,
        train_freq=1,
        gradient_steps=1,
        target_update_interval=50,
        verbose=1,
        tensorboard_log="./logs")

model.learn(int(1e3))
model.save("highway_dqn_model")