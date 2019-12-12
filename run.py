#!/usr/bin/python
import time
import socket
import paho.mqtt.client as paho
import base64
import sys
import importlib
sys.path.insert(0,'mods/')


class RunLeds(object):
    def __init__(self):
        self.devmode = 0
        self.UDP_IP = "192.168.42.148"
        self.UDP_PORT = 4242
        self.spacestate = None
        self.oldspacestate = None
        self.default = "regenboog"
        self.lampjes = "regenboog"
        self.oldlampjes = None
        self.change = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    def on_message(self,client, userdata, msg):
        if msg.topic == "hack42/state":
            self.spacestate = msg.payload
            print self.spacestate
            if self.spacestate != self.oldspacestate:
                 self.lampjes = self.default if self.spacestate == "open" else "black"
                 self.change = 1
        if msg.topic == "hack42/lampjes":
            self.lampjes = msg.payload
            if self.lampjes != self.oldlampjes:
                self.change = 1
        if msg.topic == "hack42/sidedoor/doorbell":
            self.lampjes = "geel"
            self.change = 1

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def run(self):
         self.client = client = paho.Client()
         self.client.on_message = self.on_message
         self.client.connect("127.0.0.1", 1883, 60)
         self.client.subscribe("hack42/lampjes")
         if not self.devmode:
             self.client.subscribe("hack42/state")
         self.client.subscribe("hack42/sidedoor/doorbell")
         self.client.loop_start()
         self.lampjes = self.default if self.spacestate == "open" else "black"
         while True:
             try:
                 mod = importlib.import_module(self.lampjes)
                 for (tijd, data) in getattr(mod, 'run')():
                     if self.change == 1:
                         break;
                     if self.devmode:
                         self.client.publish("loungeledemu/data",base64.b64encode(data))
                     else:
                         start = 0
                         blocksize = 1200
                         for chunk in self.chunks(data, blocksize):
                             self.sock.sendto(chr(start / 256) + chr(start % 256) + chunk, (self.UDP_IP, self.UDP_PORT))
                             start += blocksize
                         self.sock.sendto("\xFF\xFF\x00",  (self.UDP_IP, self.UDP_PORT))
                     time.sleep(tijd*(5 if self.devmode else 1) if tijd>0.04 else 0.04)
                 if self.change == 1:
                   print "Switching",self.spacestate
                   self.change = 0
                 else: 
                   self.lampjes = self.default if self.spacestate == "open" else "black"
             except KeyboardInterrupt:
                 break
             except:
                 import traceback
                 print traceback.format_exc()
                 self.lampjes = self.default if self.spacestate == "open" else "black"


leds = RunLeds()
if len(sys.argv) > 1:
    leds.default = sys.argv[1]
    leds.devmode = 1
    leds.spacestate = "open"
leds.run()
