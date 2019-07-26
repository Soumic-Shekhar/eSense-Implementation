import pexpect
import math
 
DEVICE = "00:04:79:00:0C:DA"

ACC_SCALE_FACTOR = 8192.0
G = 9.80665
GYR_SCALE_FACTOR = 65.5

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



# Start IMU Sampling
child.sendline("char-write-req 0x000c 5367020164")

#Read line of response
child.expect("Notification handle = .+\n", timeout=5)


#Parse and convert accelerometer data

acc_val = child.after[-20:-1]
print(acc_val)


def acc_convert(raw_value):
    x = int(raw_value[0:2] + raw_value[3:5], base=16)
    if x & (1 << (16-1)):
        x -= 1 << 16
    x = x / ACC_SCALE_FACTOR * G

    y = int(raw_value[6:8] + raw_value[9:11], base=16)
    if y & (1 << (16-1)):
        y -= 1 << 16
    y = y / ACC_SCALE_FACTOR * G

    z = int(raw_value[12:14] + raw_value[15:17], base=16)
    if z & (1 << (16-1)):
        z -= 1 << 16
    z = z / ACC_SCALE_FACTOR * G

    return x, y, z


acc_x, acc_y, acc_z = acc_convert(acc_val)

print("Accelerometer Values")
print("X: {}, Y: {}, Z:{}".format(acc_x, acc_y, acc_z))
print(math.sqrt(acc_x**2 + acc_y**2 + acc_z**2))




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