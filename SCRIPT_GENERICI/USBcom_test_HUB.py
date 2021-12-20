from mindstorms import MSHub
from mindstorms.control import wait_for_seconds
from hub import USB_VCP

hub = MSHub()
com = USB_VCP(0)
message = b""

while True:

    com.write(b"&Ci sono!")

    #attesa rispposta di 2 byte
    message = com.recv(2)
    message.decode('UTF-8')
    hub.light_matrix.write(str(message))
    message = b""

    if hub.left_button.was_pressed() :
        break