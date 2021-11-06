#!/usr/bin/env python3
# so that script can be run from Brickman

import sys
sys.path.append("/home/robot/Lib/site-packages/paho.mqtt.python/src/")

from ev3dev.ev3 import *
from time import sleep
from datetime import datetime
import time
import random
import json
import traceback
import paho.mqtt.client as mqtt
from threading import Thread


############################################################################
# GLOBAL VARIABLES 
############################################################################


BROKER_IP = "192.168.0.50"
CMD_TOPIC = "ev3/test"

cmd_in = "none"
cmd_out = "none"

thread_cmd = "none"

pos_pass   = 0
pos_block  = 130
pos_push   = 300
push_speed = 500


############################################################################
# MQTT RELATED
############################################################################

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(CMD_TOPIC)

def on_message(client, userdata, msg):
  
  global cmd_in,cmd_out
  
  print('\nMessage received:')
  payload = msg.payload.decode("utf-8","ignore")      
  payload = json.loads(payload) 
  print(payload)
  
#----------Commands GATE IN loop----------
  if payload["command"] == "block_in" :
    cmd_in = "block"
     
      
  if payload["command"] == "pass_in" :
    cmd_in = "pass"
    

#----------Commands GATE OUT loop----------
  if payload["command"] == "block_out" :
    cmd_out = "block"
     
      
  if payload["command"] == "pass_out" :
    cmd_out = "pass"


  if payload["command"] == "push_out" :
    cmd_out = "push"
    print("GATE OUT LOOP-- Next pallet will be \033[93mPUSHED")		#\033[93m colora di giallo


client = mqtt.Client()
client.connect(BROKER_IP)
client.on_connect = on_connect
client.on_message = on_message

############################################################################
# GATE THREAD
############################################################################

class gate (Thread):
        
        def __init__(self, nome, motor_ev3_port, sensor_ev3_port):
            Thread.__init__(self)

	    self.nome = nome
	    self.pusher = MediumMotor(motor_ev3_port)
            self.sensor = ColorSensor(sensor_ev3_port)
            
            self.sensor.mode = 'COL-REFLECT'
            self.pusher.reset()
            self.pusher.stop_action = 'hold'

	    self.last_cmd = "none"
		
            
		 
        def run(self):
            global pos_pass,pos_block,pos_push,push_speed
            global cmd_in,cmd_out,thread_cmd

            print ("Thread '" + self.nome + "' avviato")

            while True:

              if self.nome == "GATE_IN" :
		if cmd_in != self.last_cmd :
			if cmd_in == "block" : 
				self.pusher.run_to_abs_pos(position_sp = pos_block, speed_sp = push_speed) # block
				print("GATE IN LOOP-- \u001b[31mBLOCK")										#\u001b[31m colora di rosso

				if self.sensor.value() > 15 :
					print("GATE IN LOOP-- One or more pallets are waiting...")

			if cmd_in == "pass"  : 
				self.pusher.run_to_abs_pos(position_sp = pos_pass, speed_sp = push_speed)  # pass
				print("GATE IN LOOP-- \u001b[92mOPEN")										#\u001b[92m colora di verde
				
		self.last_cmd = cmd_in


              if self.nome == "GATE_OUT" :
		if cmd_out != self.last_cmd :
			if cmd_out == "block" :	
				if cmd_in == "block" : self.pusher.run_to_abs_pos(position_sp = pos_block, speed_sp = push_speed) # block
				print("GATE OUT LOOP-- \u001b[31mBLOCK")									#\u001b[31m colora di rosso

			if cmd_out == "pass" :	
				self.pusher.run_to_abs_pos(position_sp = pos_pass, speed_sp = push_speed)  # pass
				print("GATE OUT LOOP-- \u001b[92mOPEN")										#\u001b[92m colora di verde

			if cmd_out == "push" :
				if self.sensor.value() > 15 :

					sleep(0.5)
                  			self.pusher.run_to_abs_pos(position_sp = pos_push, speed_sp = push_speed)  # block
                  			sleep(1)
                  			self.pusher.run_to_abs_pos(position_sp = pos_pass, speed_sp = push_speed)  # pass
                  			sleep(0.05)
					print("GATE OUT LOOP-- Pallet has been \u001b[92mPUSHED")						#\u001b[92m colora di verde

					cmd_out = "pass"
					print("GATE OUT LOOP-- \u001b[92mOPEN")
		self.last_cmd = cmd_out

	     if thread_cmd == "q" :
		break


############################################################################
# MAIN
############################################################################ 	

gate_in = gate("GATE_IN","outA","in1")
gate_out = gate("GATE_OUT","outD","in4")

print("MENU : ")
print("-to START type \u001b[92m s")
print("-to STOP type \u001b[31m q")

while True :
	
	thread_cmd = input()

	if thread_cmd = "s" :
		client.loop_start()
		gate_in.start()
		gate_out.start()
		thread_cmd = "none"
	
	if thread_cmd = "q" :
		client.loop_stop()
		thread_cmd = "none"
		



			
			















