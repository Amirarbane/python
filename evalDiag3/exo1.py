import re

iot_frame = "SensorID:123;Temperature:25.5;Humidity:60.2;Status:OK"

sensor_id_pattern = re.compile(r'SensorID:(\d+)')
temperature_pattern = re.compile(r'Temperature:([0-9.]+)') # À compléter
humidity_pattern = re.compile(r'Humidity:([0-9.]+)') # À compléter
status_pattern = re.compile(r'Status:([A-Z.]+)') # À compléter


new_sensor_id = sensor_id_pattern.findall(iot_frame)
new_temperature_pattern = temperature_pattern.findall(iot_frame)
new_humidity_pattern = humidity_pattern.findall(iot_frame)
new_status_pattern = status_pattern.findall(iot_frame)

for sensor_id in new_sensor_id:
    print("id : ", sensor_id)


for temperature in new_temperature_pattern:
    print("température : ", temperature)


for humidity in new_humidity_pattern:
    print("Humidity : ", humidity)

for status in new_status_pattern:
    print("Status : ", status)
   
   

   