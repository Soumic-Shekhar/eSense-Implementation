import pexpect
from .utils.cal_acc import acc_convert
 
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

# Start IMU Sampling
child.sendline("char-write-req 0x000c 5367020164")

#Read line of response
child.expect("Notification handle = .+\n", timeout=5)


#Parse and convert accelerometer data

acc_val = child.after[-20:-1]
print(acc_val)

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
