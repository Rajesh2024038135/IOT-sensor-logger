import random
import csv
import time
from datetime import datetime

with open("iot_sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature", "Humidity"])

    for i in range(20):
        timestamp = datetime.now()
        temperature = round(random.uniform(20, 40), 2)
        humidity = round(random.uniform(30, 80), 2)

        writer.writerow([timestamp, temperature, humidity])
        print(timestamp, temperature, humidity)

        time.sleep(1)

print("IoT sensor data saved successfully!")