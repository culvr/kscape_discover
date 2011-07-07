#!/usr/bin/python
import socket

port = 1443	 # Kaleidescape Heartbeat Port
bufsize = 4096

def discover():
	'''Find all Kaleidescape devices on the local network'''
	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Socket
	s.settimeout(2.0) # Two second timeout
	s.bind(('', port)) # Bind to all interfaces on UDP 1443 (Kaleidescape Heartbeat)
	devices = []
		
	while True:
		try:
			data = s.recvfrom(4096)
					
		except socket.timeout:
			# No devices found
			break
		
		else:
			device_ip = data[1][0]

			if device_ip not in devices:
				devices.append(device_ip)
			else:
				# Duplicate found, no new ones will be discovered, so stop.
				break
				
	s.close()
	devices.sort()
	
	return devices

if __name__ == "__main__":
	print "Listening for Kaleidescape Devices..\n"
	
	for d in discover():
		print "Device found at: %s" % d
	



