
from collections import deque
import time


temperature = deque()
max_temp_queue = deque()


def addTemperature(current_temperature, timestamp):

    temperature.append((current_temperature, timestamp))

    while max_temp_queue and max_temp_queue[-1][0] <= current_temperature:
        max_temp_queue.pop()

    max_temp_queue.append((current_temperature, timestamp))

    expire_old_temperatures(timestamp)

def expire_old_temperatures(current_time):

    while temperature and temperature[0][1] <= current_time - 86400:
        expired_temp = temperature.popleft()

        if max_temp_queue and max_temp_queue[0] == expired_temp:
            max_temp_queue.popleft()

def get_max_temp():
    if max_temp_queue:
        return  max_temp_queue[0][0]
    else:
        return None


current_time = int(time.time())


addTemperature(30, current_time - 86000)  # 23 hours ago
addTemperature(25, current_time - 85000)  # Just under 24 hours ago
addTemperature(40, current_time)          # Current time
addTemperature(35, current_time + 100)    # Future temperature

print("Max temperature in the last 24 hours:", get_max_temp())