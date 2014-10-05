from kivy.app import App
from kivy.uix.button import Button
import socket

class MainApp(App):

    def build(self):
        return Button(text = 'Hello World')

if __name__ == '__main__':
    MainApp().run()
