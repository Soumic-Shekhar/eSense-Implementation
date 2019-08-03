import pexpect
import math
from utils.cal_acc import acc_convert
import datetime
import logging
from pynput.mouse import Controller

LOG_FILENAME = "{}.log".format(datetime.datetime.now().strftime("%c"))

MOUSE_SPEED = 1

mouse = Controller()


DEVICE = "00:04:79:00:0C:DA"
print(DEVICE)

# Run gatttool interactively.

print("Run gatttool...")
child = pexpect.spawn("gatttool -I")
 
# Connect to the device.

print("Connecting to "),
print(DEVICE),
child.sendline("connect {0}".format(DEVICE))
child.expect("Connection successful", timeout=5)
print(" Connected!")

#Create file for logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename = LOG_FILENAME)

# Start IMU Sampling
child.sendline("char-write-req 0x000c 5367020164")


def mouse_move(x, y):
    
    x = x * abs(x) * MOUSE_SPEED
    y = y * abs(y) * MOUSE_SPEED
    
    mouse.move(x, y)

while True:

    #Read line of response
    child.expect("Notification handle = .+\n", timeout=5)

    #Parse and convert accelerometer data

    acc_val = child.after[-20:-1]
    print(acc_val)

    acc_x, acc_y, acc_z = acc_convert(acc_val)
    
    mouse_move(acc_z, acc_y)
    
    output = "X: {}, Y: {}, Z: {}".format(acc_x, acc_y, acc_z)
    logging.info(output)

    print("Accelerometer Values")
    print(output)
#    print(math.sqrt(acc_x**2 + acc_y**2 + acc_z**2))

#Stop IMU Sampling

child.sendline("char-write-req 0x000c 5302020000")
child.expect(r"\[{}\].+\n".format(DEVICE), timeout=5)
print("*")
print(child.after)
print("*")

# Disconnect

print("Disconnecting... "),
child.sendline("disconnect")
child.expect("\n", timeout=5)
print(" Disconnected")
