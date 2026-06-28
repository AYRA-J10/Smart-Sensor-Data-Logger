import numpy as np

class Sensor:

    def __init__(self, real_temperature, noise_std):
        self.real_temperature = real_temperature
        self.noise_std = noise_std

    def read(self):
        noise = np.random.normal(0, self.noise_std)
        return self.real_temperature + noise