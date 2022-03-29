from CLASSE_GUI import GUI
from CLASSE_CLIENT import MQTT_Network
import time


def main():

    client = MQTT_Network()
    gui = GUI()

    client.MQTT_client_start()
    gui.start_GUI()

    time.sleep(30)
    client.MQTT_client_stop()



if __name__ == "__main__":
    main()


    '''
    client.Print_Attributes()
    client.MQTT_client_start()
    time.sleep(3)
    client.publish_msg("start TEST")
    time.sleep(3)
    client.MQTT_client_stop()
    '''