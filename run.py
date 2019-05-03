#!/usr/bin/python
import time
import socket
import paho.mqtt.client as paho
import mods

class RunLeds(object):
    def __init__(self):
        self.UDP_IP = "192.168.42.148"
        self.UDP_PORT = 4242
        self.spacestate = None
        self.oldspacestate = None
        self.lampjes = "regenboog"
        self.oldlampjes = None
        self.change = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    def on_message(self,client, userdata, msg):
        if msg.topic == "hack42/state":
            self.spacestate = msg.payload
            print self.spacestate
            if self.spacestate != self.oldspacestate:
                 self.lampjes = "regenboog" if self.spacestate == "open" else "black"
                 self.change = 1
        if msg.topic == "hack42/lampjes":
            self.lampjes = msg.payload
            if self.lampjes != self.oldlampjes:
                self.change = 1
        if msg.topic == "hack42/sidedoor/doorbell":
            self.lampjes = "geel"
            self.change = 1

    def run(self):
         self.client = client = paho.Client()
         self.client.on_message = self.on_message
         self.client.connect("192.168.142.66", 1883, 60)
         self.client.subscribe("hack42/lampjes")
         self.client.subscribe("hack42/state")
         self.client.subscribe("hack42/sidedoor/doorbell")
         self.client.loop_start()
         self.lampjes = "regenboog" if self.spacestate == "open" else "black"
         while True:
             try:
                 themod = getattr(mods, self.lampjes)
                 thefunc = getattr(themod, 'run')
                 for (tijd, data) in thefunc():
                     if self.change == 1:
                         break;
                     self.sock.sendto(data, (self.UDP_IP, self.UDP_PORT))
                     time.sleep(tijd if tijd>0.09 else 1)
                 if self.change == 1:
                   print "Switching",self.spacestate
                   self.change = 0
                 else: 
                   self.lampjes = "regenboog" if self.spacestate == "open" else "black"
             except:
                 import traceback
                 print traceback.format_exc()
                 self.lampjes = "regenboog" if self.spacestate == "open" else "black"


leds = RunLeds()
leds.run()
