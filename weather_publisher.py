import paho.mqtt.client as mqtt
import logging

def publish_weather(host, topic, username, password, message):
    logging.info(f"Publishing weather data to {topic} at {host}")
    # Create a client instance
    client = mqtt.Client()

    client.username_pw_set(username, password)
    # Connect to the broker
    client.connect(host, 1883)

    # Publish a message to a topic
    info = client.publish(topic, message)
    #logging.debug(info.is_published())

    # Disconnect from the broker
    client.disconnect()

    logging.info("Successfully published weather data")