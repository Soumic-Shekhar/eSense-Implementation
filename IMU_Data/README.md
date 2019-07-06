# eSense BLE 
## Research on HID devices and there use case at North South University(NSU)
### Shell Script for reading IMU Data from the eSense BLE in-ears (PLUG&PLAY)

Requirements:
- Linux [Tested on Ubuntu 18.04]
- Bluetooth
- hcitool
- gattool

The commandline tools used come pre packaged with installation of linux. Before running the code make sure your bluetooth device agent in detected by the OS. Run `hcitool dev` and `gatttool` form terminal to make sure they are present and bluetooth agent is detected.

Run:
```bash
git clone https://github.com/Soumic-Shekhar/eSense-Implementation.git
cd /path/to/eSense-Implementation/IMU_Data
./eSense.sh
```
