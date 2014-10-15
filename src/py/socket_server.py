# Echo server program
import logging
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

class SocketServer(object):
    
  def __init__(self, host=HOST, port=PORT):
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server.bind((host, port))

  def RunServer(self):
    self.server.listen(1)
    conn, addr = self.server.accept()

    while True:
      data = conn.recv(1024)
        if not data:
          break

    conn.close()

