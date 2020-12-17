# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import os
import bluetooth._bluetooth as bluez
import time

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "********* Gateway Ble Scanning thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------------------Scanning......."
	for beacon in returnedList:
                print "\n"
                print "----------------------Find uuid......"
                print beacon
		print "[Current time sent to Server]"
                now = time.localtime()
                print "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                os.system("./objectCommand.sh")
                print "\n"
		#print beacon

