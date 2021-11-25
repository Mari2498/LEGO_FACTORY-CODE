import paho.mqtt.client as mqtt
import json

""" 
Structure example:
----------EV3 JSON MSG CONFIG----------

TOPICS :

    ev3/dc_log :

        json_payload_example = {
            "sens_type" : "opt",    #type of ev3 sensor
            "sens_num" : 1          #number of a specific kind of sensor
        } 
"""

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    #write topics here :
    #example : 
    #client.subscribe("NOME_TOPIC") 

def on_message(client, userdata, msg):
    print('\nMessage received:')
    payload = msg.payload.decode("utf-8","ignore")      # transform payload into str
    payload = json.loads(payload)                       # transforms payload into dict 
    print (msg.topic)
    print (payload)
    
    #example :
    #if msg.topic == "NOME_TOPIC" :
    #
    #    sens_type = payload["sens_type"]
    #    sens_num = payload["sens_num"]

# The callback for SUBSCRIBE.
def on_subscribe(client, userdata, mid, granted_qos):
    print('Successfully subscribed!')

# The callback for when a PUBLISH message is sent to the broker.
def on_publish(client, userdata, mid):
    print("Message has been published.")

if __name__ == "__NOmain__":

    """ 
    #MQTT 
    #IP ADDRESS of Mosquitto device
    IP_BROKER = input("\nInsert broker IP : ")
    print("\n")

    #Client functions
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    #Connection to broker
    client.connect(IP_BROKER)

    #Client loop start
    client.loop_forever() 
    
    """

    """ 
    You can use also :

    client.loop_start()
    client.loop_stop()

    """

    """
    To publish msg :

    topic = "photon/setup"

    payload_out_setup = {"setup" : "SETUP", "nome_phtn" : "PHTN_IN"}
    payload_out_setup = json.dumps(payload_out_setup, indent=4)
    client.publish(topic, payload_out_setup, 2)

    
    """

