import paho.mqtt.client as mqtt
import Adafruit_DHT
import json
import time
import threading

# Set the GPIO pin for the DHT11 sensor
sensor_pin = 17

def read_dht11():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, sensor_pin)
    return humidity, temperature

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def publish_sensor_data(client):
    while True:
        humidity, temperature = read_dht11()

        # Prepare sensor data as JSON payload
        sensor_data = {
            'temperature': temperature,
            'humidity': humidity
        }

        # Convert the dictionary to a JSON string
        payload = json.dumps(sensor_data)

        # The four parameters are topic, sending content, QoS, and whether retaining the message respectively
        client.publish('raspberry/latihan123', payload=payload, qos=0, retain=False)
        print(f"Sent sensor data: {payload} to raspberry/latihan123")

        # Wait for 1 second before sending the next reading
        time.sleep(1)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

# Start a separate thread for publishing sensor data
publish_thread = threading.Thread(target=publish_sensor_data, args=(client,))
publish_thread.start()
client.loop.forever()

# Call the function to publish sensor data
publish_sensor_data(client)
