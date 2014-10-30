
#from kivy.support import install_twisted_reactor
#install_twisted_reactor()

#from twisted.web.xmlrpc import Proxy
#from twisted.internet import reactor

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import *

import xmlrpclib

class RunningRoad(Widget):
  def __init__(self, velocity=1, **kwargs):
    self.speed = velocity * 0.05
    self.l1 = 0 
    super(RunningRoad, self).__init__(**kwargs)
    Clock.schedule_interval(self.update, 1/24.)
    Clock.schedule_interval(self.getSpeed, 1)

  def update(self, *args):
    
    self.l1 += self.speed
    spd = self.l1 - int(self.l1) 
    self.canvas.clear()
    xmg = self.center_x * 0.75
    ymg = self.center_y * 0.75
    with self.canvas:
      Color(255, 255, 0)
      Line(points=[0, self.center_y*0.75, self.width, self.center_y*0.75])
      Line(points=[0, 0, self.center_x * 0.75, self.center_y * 0.75])
      Line(points=[self.width, 0, self.center_x * 1.25, self.center_y * 0.75])
      Line(points=[self.center_x, 0, self.center_x, self.center_y * 0.75])
      Line(points=[self.center_x * 0.5, 0, self.center_x * 7/8., self.center_y * 0.75])
      Line(points=[self.center_x * 1.5, 0, self.center_x * 9/8., self.center_y * 0.75])
      Line(points=[xmg - spd*xmg, self.center_y*0.75-spd*ymg, self.center_x*1.25+spd*xmg, self.center_y*0.75-spd*ymg])

  def set_speed(self, v):
    self.speed = v * 0.05

  def getSpeed(self, *args):
    s = xmlrpclib.Server('http://192.168.43.58:8000/')
    self.speed = s.speed() * 0.0005

class roadClientApp(App):
  def build(self):
    #proxy = Proxy('http://192.168.43.58:8000/')
    #proxy.callRemote('speed').addCallbacks(printValue, printError)
    #reactor.run()
    #s = xmlrpclib.Server('http://192.168.43.58:8000/')
    #reactor.listenTCP(8000, EchoFactory(self))
    #y = s.speed()
    self.road = RunningRoad(velocity = 2)     
    return self.road


def printValue(value):
    print repr(value)
    reactor.stop()

def printError(error):
    print 'error', error
    reactor.stop()

if __name__ == '__main__':
  roadClientApp().run()
