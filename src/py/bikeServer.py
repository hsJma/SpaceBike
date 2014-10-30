
from twisted.internet import reactor, protocol
from twisted.web import xmlrpc, server

from threading import Thread

import RPi.GPIO as GPIO
import time

class bikeServer(xmlrpc.XMLRPC):
  def xmlrpc_speed(self):
    return SPD


def GetSpeed():
  GPIO.setmode(GPIO.BOARD)
  hall_PIN = 11
  TIME_LAPSE = 0.3
  GPIO.setup(hall_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  previousTime = time.time()

  try :
    while True:
      currentTime = time.time()
      d_time = currentTime - previousTime
      if GPIO.input(hall_PIN) == GPIO.LOW and d_time > TIME_LAPSE :
        previousTime = currentTime
        spd = int(60 / d_time)
        global SPD 
        SPD = spd
        print SPD
        #return spd

  except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

  finally:
    GPIO.cleanup()


def main():
  t = Thread(target=GetSpeed)
  t.daemon = True
  t.start()
  print 'yo'

  r = bikeServer()
  reactor.listenTCP(8000, server.Site(r))
  reactor.run()

if __name__ == '__main__':
  main()
