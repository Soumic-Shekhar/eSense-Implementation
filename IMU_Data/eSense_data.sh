#!/bin/bash

#eSense BLE Sensor Data

echo 'Initializing -->' 

#declare -a IMU_Val #not implimented
#find active eSense Devices
devices="$(hcitool scan&)" 
echo "$devices"
eSense="$(echo "$devices" | grep 'eSense-0')"
echo "$eSense"
#get MAC address of the device
eSenseMAC="$(echo "$eSense" | grep -o '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}')"
echo "$eSenseMAC"

# Activate IMU 
gatttool -b "$eSenseMAC" --char-write-req -a '0x000c' -n 5367020164
# Get IMU readings
IMU_HEX(){
	
	HEX_Data="$(gatttool -b "$eSenseMAC" --char-read -a '0x000e')"
	echo "${HEX_Data:33}" # data starts at pos 33
	# IMU_Val+=(HEX_Data) # not implemented
}
	


char_val=$(IMU_HEX) #raw values (2*Data + #Data)
echo "$char_val"
acc="${char_val:30}" #raw acc values starts as pos 30 --> raw data
echo "$acc"
# .py scrips to convert acceleration hex to decimal
python src/utils/cal_acc.py "$acc"

