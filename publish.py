import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    for i in range(5):
        client.publish('raspberry/latihan123', payload= "asasasa",  qos=0, retain=False)
        print(f"asdasdadsa")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()
