from CLASSE_CLIENT import MQTT_Network
import time

def main():

	client = MQTT_Network()
	client.Print_Attributes()
	client.MQTT_client_start()
	time.sleep(3)
	client.MQTT_client_stop()



if __name__ == "__main__":
	main()