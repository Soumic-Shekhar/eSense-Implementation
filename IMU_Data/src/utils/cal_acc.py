import math

# calculate accelerometer values of eSense IMU

def acc_convert(raw_value):

	ACC_SCALE_FACTOR = 8192.0
	G = 9.80665
	GYR_SCALE_FACTOR = 65.5

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

if __name__ == "__main__":
	import sys
	try:
		print (acc_convert(sys.argv[1]))
	except:
		print("--hex string missing")
