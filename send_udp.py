from __future__ import print_function
import socket
import time
from contextlib import closing

import Leap, sys

class SampleListener(Leap.Listener):
	def on_init(self, controller):
		print ("Leap Initialized")


	def on_connect(self, controller):
		print ("Leap Connected")

	def on_disconnect(self, controller):
		print ("Leap Disconnected")

	def on_exit(self, controller):
		print ("Leap Exited")

	def on_frame(self, controller):
		#Get the most recent frame and send UDP
		frame = controller.frame()
		if not frame.hands.is_empty:
			hand = frame.hands[0]
			fingers = hand.fingers
			if not fingers.is_empty:
				avg_pos = Leap.Vector()
				for finger in fingers:
					avg_pos += finger.tip_position
				avg_pos /= len(fingers)
				print ("Hand has %d fingers, average finger tip position: %s" %(len(fingers), avg_pos))






def main():
	#host = '127.0.0.1'
	host = '10.0.2.15'
	port = 4000
	count = 0
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	listener = SampleListener()
	controller = Leap.Controller()
	controller.add_listener(listener)

	print ("Press Enter to quit...")
	sys.stdin.readline()
	controller.remove_listener(listener)

	#with closing(sock):
	#	while True:
	#		message = 'Hello world : {0}'.format(count).encode('utf-8')
	#		print(message)
	#		sock.sendto(message, (host, port))
	#		count += 1;
	#		time.sleep(1)
	return

if __name__ == '__main__':
	main()