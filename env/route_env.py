import gym
import numpy as np
from gym import spaces
from env.energy_model import estimate_energy, energy_to_co2

class CarbonRouteEnv(gym.Env):
    """Toy environment for carbon-aware routing"""
    def __init__(self, n_nodes=5, vehicle_type='diesel'):
        super().__init__()
        self.n_nodes = n_nodes
        self.vehicle_type = vehicle_type

        # Action: pick next node (0..n_nodes-1)
        self.action_space = spaces.Discrete(self.n_nodes)
        # Observation: current node + remaining deliveries as binary vector
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.n_nodes+1,), dtype=np.float32)

        # Synthetic distance & grade matrix
        self.dist_matrix = np.random.uniform(1, 10, (n_nodes, n_nodes))
        self.grade_matrix = np.random.uniform(-5, 5, (n_nodes, n_nodes))

    def reset(self):
        self.current_node = 0
        self.remaining = set(range(1, self.n_nodes))
        return self._get_obs()

    def _get_obs(self):
        obs = np.zeros(self.n_nodes+1, dtype=np.float32)
        obs[0] = self.current_node / (self.n_nodes-1)
        for r in self.remaining:
            obs[r] = 1.0
        return obs

    def step(self, action):
        if action not in self.remaining:
            # Invalid or revisiting → penalty
            return self._get_obs(), -50.0, False, {}

        distance = self.dist_matrix[self.current_node, action]
        grade = self.grade_matrix[self.current_node, action]

        energy = estimate_energy(distance, grade, self.vehicle_type)
        co2 = energy_to_co2(energy, self.vehicle_type)

        reward = -co2  # we minimize CO2

        self.current_node = action
        self.remaining.remove(action)

        done = len(self.remaining) == 0
        return self._get_obs(), reward, done, {"co2": co2}
