import time
import yaml
from colorama import Fore, Style
from scapy.all import IP, TCP, sr1


# the time to wait between sending each packet in seconds
time_between_packets_in_seconds = 5

# colors
SUCCESS_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
INFO_COLOR = Fore.BLUE

# print in colors
def c_print(string, color = Fore.BLUE):
	print(color + string + Style.RESET_ALL)

# default values
try:
	with open("./configs.yaml", "r") as f:
		configs = yaml.safe_load(f)
		dst = configs["CONFIGS"]["dst"]
		dport = configs["CONFIGS"]["dport"]
		
except Exception as e:
	c_print(f"Error - {str(e)}\n", ERROR_COLOR)
	dst="127.0.0.1"
	dport=5000

c_print(f"Loaded default values")
c_print(f"dst {dst}")
c_print(f"dport {dport}\n")

# create a packet with customized dst and dport(with default values)
def create_packet(dst=dst, dport=dport):
	return IP(dst=dst)/TCP(dport=dport)

# send and wait for the response of the packet we created with a timeout of 2s
def send_and_wait_for_response(packet, timeout=2):
	return sr1(packet, timeout=timeout)

# check if we got a successful ACK response
def is_ack_successfully(response):
	if(response.haslayer(TCP)):
		tcp_layer = response.getlayer(TCP)
		if tcp_layer.flags == "SA":
			c_print(f"Successfully Ack - {tcp_layer.flags}", SUCCESS_COLOR)
		else:
			c_print(f"Didn't Ack - {tcp_layer.flags}", ERROR_COLOR)
	else:
		c_print("Not a TCP packet", ERROR_COLOR)

# handle the response output
def handle_response(response):
	if(response):
		c_print(f"Received Response for #{packet_num}", SUCCESS_COLOR)
		is_ack_successfully(response)
	else:
		c_print(f"No Response for #{packet_num}", ERROR_COLOR)

# looping and sending packets
packet_num = 1
while True:
	# create a packet
	packet = create_packet()
	c_print(f"Sending #{packet_num} - {packet}", INFO_COLOR)
	# send and wait for response
	response = send_and_wait_for_response(packet)
	# handle the response
	handle_response(response)


	packet_num += 1
	time.sleep(time_between_packets_in_seconds) # sleep for 5 seconds before sending another one
