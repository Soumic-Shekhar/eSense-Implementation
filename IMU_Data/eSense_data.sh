#!/bin/bash

#eSense BLE Sensor Data

declare -a IMU_Val

devices="$(hcitool scan&)"
echo "$devices"

eSense="$(echo "$devices" | grep 'eSense-0')"
echo "$eSense"

eSenseMAC="$(echo "$eSense" | grep -o '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}')"
echo "$eSenseMAC"

# Activate IMU 
gatttool -b "$eSenseMAC" --char-write-req -a '0x000c' -n 5367020164

IMU_HEX(){
	
	HEX_Data="$(gatttool -b "$eSenseMAC" --char-read -a '0x000e')"
	# IMU_Val+=(HEX_Data)
}
	

for (( ; ; ))
	do
		IMU_HEX
		echo $HEX_Data
	done

