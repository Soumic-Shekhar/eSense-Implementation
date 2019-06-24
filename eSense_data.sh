#!/bin/bash

#eSense BLE Sensor Data

devices=$(bluetoothctl&)
echo "$devices" | grep "eSense"
#echo "$eSense"
