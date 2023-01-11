import random
from paho.mqtt import client as mqtt_client
import ssl
import time 

broker = "mqtt.xingest.durbinservices.com"
port = 8883
# topic = "Durbin/python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'durbin-mqtt-broker-user'
password = 'z3sd58PkSVYAubUkTPpQNTBZRyRcN8Qf2eQVVcmGX7ga'

topic = [
    "maco/maco-mining/Mining-Ping/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Fire-Detection/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Nitrogen-Fault/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Nitrogen-Release/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Gps-Location/7a0b067f-bc20-4c1d-9a69-bac7c3484242"
]

new_topic = "maco-new/maco-mining/Mining-new/7a0b067f-bc20-4c1d-9a69-bac7c3484242"

global arr
arr=[]

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.tls_set("./isrgroot.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
    client.tls_insecure_set(True)
    client.connect(broker, port)
    return client

def combined_data_publish(client):
    while True:
        time.sleep(5)
        global arr
        print(arr)
        v = ""
        for i in range (len(arr)):
           v = v + arr[i] 

        result = client.publish(new_topic, v)
        print(result)
        arr = [] 
def subscribe(client: mqtt_client):
    global arr
    arr = []
    def on_message(client, userdata, msg):
        arr.append(msg.payload.decode())
        # print(arr)
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    for i in range (4):
            
            client.subscribe(topic[i])

    client.on_message = on_message

        

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start() 
    combined_data_publish(client)


# if __name__ == '__main__':
#     run()