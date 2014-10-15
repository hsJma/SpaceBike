from kivy.app import App
from kivy.uix.button import Button
from kivy.support import install_twisted_reactor
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import *


class RunningRoad(Widget):
  def __init__(self, velocity=1, **kwargs):
    self.speed = velocity * 0.05
    self.l1 = 0
    super(RunningRoad, self).__init__(**kwargs)
    Clock.schedule_interval(self.update, 1/24.)

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
    self.speed = v


install_twisted_reactor()
from twisted.internet import reactor
from twisted.internet import protocol

class EchoProtocol(protocol.Protocol):
  def dataReceived(self, data):
    response = self.factory.app.handle_message(data)
    if response:
      print response
      self.transport.write(response)

class EchoFactory(protocol.Factory):
  protocol = EchoProtocol
  def __init__(self, app):
    self.app = app


from kivy.app import App
from kivy.uix.label import Label

class TwistedServerApp(App):
  def build(self):
    self.label = Label(text="server started\n")
    reactor.listenTCP(8000, EchoFactory(self))
    #return self.label
    return RunningRoad(velocity = 0.5)     
        

  def handle_message(self, msg):
    self.label.text  = "received:  %s\n" % msg

    if msg == "ping":  msg =  "pong"
    if msg == "plop":  msg = "kivy rocks"
    self.label.text += "responded: %s\n" % msg
    return msg


if __name__ == '__main__':
  TwistedServerApp().run()

