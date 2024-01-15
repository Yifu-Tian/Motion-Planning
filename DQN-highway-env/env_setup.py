'''
Create and configure the environment
'''

import gymnasium as gym
import highway_env

def create_env():
    '''
    Choose scenario
    1. highway-v0 / highway-fast-v0
    2. merge-v0
    3. roundabout-v0
    4. parking-v0
    5. intersection-v0
    6. racetrack-v0
    
    Choose mode: "rgb_array"
    '''
    env = gym.make("highway-fast-v0", render_mode = "rgb_array") 
    return env