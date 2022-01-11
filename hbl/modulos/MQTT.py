# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client
from modulos import salidas as salidas
from modulos import hbl as hbl


broker = 'broker.mqttdashboard.com'
port = 1883
TopicSend = "RPI/JPH/HBL/Send"
TopicRecv = "RPI/JPH/HBL/Recv"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    time.sleep(1)
    msg = f"messages: {msg_count}"
    result = client.publish(TopicSend, msg)
    # result: [0, 1]
    status = result[0]
    #if status == 0:
        #print(f"Send `{msg}` to topic `{TopicSend}`")
    #else:
        #print(f"Failed to send message to topic {TopicSend}")
    #msg_count += 1


def subscribe(client: mqtt_client,pi):
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.payload.decode() == "ON":
            pi.write(hbl.DIG_out_pin_out1, hbl.ON)
        if msg.payload.decode() == "OFF":
            pi.write(hbl.DIG_out_pin_out1, hbl.OFF)

    client.subscribe(TopicRecv)
    client.on_message = on_message

def inicializacion():
    client = connect_mqtt()
    client.loop_start()
    return client
