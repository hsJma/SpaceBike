# Echo server program
import logging
import socket


HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
logging.info('Start listening')
s.listen(1)

conn, addr = s.accept()
logging.info('Connected by %r', addr)

while True:
  data = conn.recv(1024)
  # client clost
  if not data:
    break
  logging.info('Got data %r', data)
  #conn.sendall(data)

logging.info('Close server')
conn.close()
