# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client
from modulos import salidas as salidas
from modulos import hbl as hbl
import json
import os
from modulos import auxiliar as auxiliar
from modulos import variablesGlobales as variablesGlobales


# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    auxiliar.EscribirFuncion("connect_mqtt")

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(hbl.MQTT_broker, hbl.MQTT_port)
    return client


def publish(client,msg):
    auxiliar.EscribirFuncion("publish")

    time.sleep(1)
    result = client.publish(hbl.MQTT_TopicSend, msg)
    # result: [0, 1]
    status = result[0]
    #if status == 0:
        #print(f"Send `{msg}` to topic `{TopicSend}`")
    #else:
        #print(f"Failed to send message to topic {TopicSend}")
    #msg_count += 1


def subscribe(client: mqtt_client,pi):
    auxiliar.EscribirFuncion("subscribe")

    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.payload.decode() == "ON":
            pi.write(Pin_Salida1, hbl.ON)
        if msg.payload.decode() == "OFF":
            pi.write(Pin_Salida1, hbl.OFF)

    client.subscribe(hbl.MQTT_TopicRecv)
    client.on_message = on_message

def inicializacion():
    auxiliar.EscribirFuncion("inicializacion")

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 
    with open(os.path.join(__location__ , 'hbl.json'), "r") as f:
        data = json.load(f)
    client = connect_mqtt()
    client.loop_start()
    publish(client,json.dumps(data))
    return client
