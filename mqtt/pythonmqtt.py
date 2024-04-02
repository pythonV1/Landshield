import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, message):
    print("Received message:", str(message.payload.decode("utf-8")))

def publish_message(client, topic, message):
    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"Published message to topic '{topic}': {message}")
    else:
        print(f"Failed to publish message to topic '{topic}'")

def subscribe_topic(client, topic):
    client.subscribe(topic)
    print(f"Subscribed to topic: {topic}")

def run_mqtt_client():
    server = "mqtt.marakayar.com"
    port = 1883
    username = "user"
    password = "Password#1234"
    client_id = "python_client"  # You can set any client ID here

    topic_to_publish = "speed-queen/laundry/604fef25bf58/subscribe"
    topic_to_subscribe = "speed-queen/laundry/604fef25bf58/publish"

    client = mqtt.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(server, port)
    except ConnectionRefusedError:
        print("Connection failed. Please check your MQTT Broker.")
        return

    client.loop_start()

    publish_message(client, topic_to_publish, "hello")

    time.sleep(5)

    subscribe_topic(client, topic_to_subscribe)

    time.sleep(10)  # Listen for messages for 10 seconds

    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    run_mqtt_client()
