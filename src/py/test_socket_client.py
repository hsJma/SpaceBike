# Echo client program
import logging
import socket
import time

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
DATA = 'test_data/speeds.txt'

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logging.info('Connecting to %r:%r', HOST, PORT)
s.connect((HOST, PORT))

speeds = []
with open(DATA,'r') as f:
  speeds = f.readlines()

for speed in speeds:
  time.sleep(1)
  speed_to_send = speed.strip()
  logging.info('Client send peed %r', speed_to_send)
  s.sendall(speed_to_send)
  #data = s.recv(1024)
  #logging.info('Client received %r', data)

logging.info('Close client')
s.close()
