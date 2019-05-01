#!/usr/bin/env python
import time
import random

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
try:
    client.connect("localhost", 1883, 60)
    client.loop_start()

    while True:
        time.sleep(1)
        # Randomnumber for Temp !
        temp_random =  random.randint(1,100)
        print(temp_random)
        client.publish("test/temperature", temp_random)
except:
    print ("no local MQTT Broker found !")
    print ("Start with bash command brew services start mosquitto")