import serial

ser = serial.Serial()
ser.port = '/dev/ttyACM0'

message = b""
ser.open()

while True:
	
	message = ser.read(1)
	if message == b"&" :
		message = ser.read(8)
		print(message)

		if message == b"Ci sono!":
			ser.write(b"Ok")

ser.close()
