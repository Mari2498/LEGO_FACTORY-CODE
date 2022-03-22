import paho.mqtt.client as mqtt
import json
import time


class MQTT_Network():

	def __init__ (self):
		self.client = mqtt.Client()
		#load setup file (JSON fomat)
		setup_file = open("MQTT_SETUP.txt")
		self.setup = json.load(setup_file)
		setup_file.close()
		#Set attributes
		self.BROKER_IP = self.setup["broker_ip"]
		self.topics = self.setup["topics"]

	# Debug function to print all class attrs
	def Print_Attributes(self):
		print(self.BROKER_IP)
		print(self.topics)

	# The callback for broker CONNECTION
	def on_connect(self, client, userdata, flags, rc):
		print( "Connected with result code " + str(rc) )
		#topics subscriptions
		client.subscribe(self.topics["general_topic"])

	# The callback for SUBSCRIBE
	def on_subscribe(self, client, userdata, mid, granted_qos):
		print('Successfully subscribed!')

	# Function to publish messages on network
	def publish_msg(self):
		

	# Client thread start function
	def MQTT_client_start(self):
		self.client.on_connect = self.on_connect
		#self.client.on_message = self.on_message
		self.client.on_subscribe = self.on_subscribe
		#self.client.on_publish = self.on_publish
		self.client.connect(self.BROKER_IP)
		self.client.loop_start()
		print("MQTT network started")

	# Client thread start function
	def MQTT_client_stop(self):
		self.client.loop_stop()
		print("MQTT network stopped")












'''
	# The callback for when a message arrives from the broker.
	def on_message(self, client, userdata, msg):
		print("\nMessage received:")
		payload = msg.payload.decode("utf-8","ignore")      
		payload = json.loads(payload)                       
		print (msg.topic)
		print (payload)

		if self.Check_Internal_Network_Dev(payload["name_dev"]) :

			if msg.topic == self.topics["request_topic"] :

				rqst_name_dev = payload["name_dev"]
				rqst_type = payload["data"]["rqst_type"]
				rqst_data = payload["data"]["rqst"]

				return rqst_name_dev, rqst_type, rqst_data 



	# The callback for when a PUBLISH message is sent to the broker.
	def on_publish(self, client, userdata, mid):
		print("Message has been published.")

	def Send_Reply(self, rqst_name_dev, rqst_type, rqst_data):
		payload_out = {
			"name_dev": 			self.Name_dev_controller,
			"data":
			{
				"rqst_name_dev":	rqst_name_dev,
				"rply_type":		rqst_type,
				"rply":				rqst_data
			}
		}
		
		payload_out = json.dumps(payload_out, indent=4)
		self.client.publish(self.topics["reply_topic"], payload_out, 2)

	def Test_request(self):
		payload_out = {
			"name_dev": 			"EV3-1",
			"data":
			{
				"rqst_type":		"color",
				"rqst":				"yellow"
			}
		}
		
		payload_out = json.dumps(payload_out, indent=4)
		self.client.publish(self.topics["request_topic"], payload_out, 2)


if __name__ == "__main__":

	net = MQTT_Network()
	net.MQTT_client_start()

	net.Send_Reply("EV3-1","Cmd","Start")
	net.Test_request()

	time.sleep(10)

	net.MQTT_client_stop()

'''