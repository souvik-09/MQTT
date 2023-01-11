import random
import time
from paho.mqtt import client as mqtt_client
import ssl

broker = "mqtt.xingest.durbinservices.com"
port = 8883
# topic = "Durbin/python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'durbin-mqtt-broker-user'
password = 'z3sd58PkSVYAubUkTPpQNTBZRyRcN8Qf2eQVVcmGX7ga'

topic = [
    "maco/maco-mining/Mining-Ping/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Fire-Detection/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Nitrogen-Fault/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Nitrogen-Release/7a0b067f-bc20-4c1d-9a69-bac7c3484242",
    "maco/maco-mining/Gps-Location/7a0b067f-bc20-4c1d-9a69-bac7c3484242"
]

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


def publish(client):
    msg_count = 0
    while True:
        time.sleep(3)
        for i in range (4):
        
            msg = f"messages: {msg_count}"
            
            # print(msg)
            # print(topic[i])
            result = client.publish(topic[i], msg)
            # msg_count+=1
        
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic[i]}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()