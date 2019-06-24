#!/bin/bash

#eSense BLE Sensor Data

devices=$(bluetoothctl&)
eSense="$(echo "$devices" | grep 'eSense')"
echo "$eSense"
eSenseMAC="$(echo "$eSense" | grep -o '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}')"
echo "$eSenseMAC"

gatttool -b "$eSenseMAC" --char-write-req -a '0x000c' -n 5367020164 --listen
#gatttool -b "$eSenseMAC" --char-read -a 0x000c

#gatttool --help-all
