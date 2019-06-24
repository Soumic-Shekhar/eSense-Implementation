#!/bin/bash

#eSense BLE Sensor Data

devices=$(bluetoothctl&)
eSense="$(echo "$devices" | grep 'eSense')"
eSenseMAC="$(echo "$eSense" | grep -o '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}')"
echo "$eSenseMAC"
