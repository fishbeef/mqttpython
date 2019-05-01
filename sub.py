#!/usr/bin/env python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("test/#")

def on_message(client, userdata, msg):
    print("Read from topic: " + msg.topic + "- with payload / value : " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
try:
    client.connect("localhost", 1883, 60)
    client.loop_forever()
except:
    print ("no local MQTT Broker found !")
    print ("Start with bash command brew services start mosquitto")