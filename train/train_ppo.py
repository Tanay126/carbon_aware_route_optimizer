import gym
from stable_baselines3 import PPO
from env.route_env import CarbonRouteEnv

def main():
    env = CarbonRouteEnv(n_nodes=5, vehicle_type='diesel')
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=5000)
    model.save('ppo_carbon_route')
    print('Training complete. Model saved as ppo_carbon_route.zip')

if __name__ == '__main__':
    main()
