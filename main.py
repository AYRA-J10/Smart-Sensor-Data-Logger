import matplotlib.pyplot as plt

from sensor import Sensor
from sensor_pipeline import SensorPipeline
from config import *

sensor = Sensor(
    REAL_TEMPERATURE,
    NOISE_STD
)

pipeline = SensorPipeline(
    THRESHOLD,
    SMOOTHING_FACTOR
)

pipeline.run(sensor, NUM_READINGS)

plt.figure(figsize=(10,5))

plt.plot(
    pipeline.raw_data,
    label="Raw Sensor"
)

plt.plot(
    pipeline.smooth_data,
    label="Smoothed"
)

plt.title("Smart Sensor Data Logger")

plt.xlabel("Reading Number")

plt.ylabel("Temperature")

plt.legend()

plt.grid()

plt.show()