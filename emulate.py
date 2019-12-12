#!/usr/bin/python
import time
import paho.mqtt.client as paho
import mods
import base64

class RunLeds(object):
    def __init__(self):
        self.lampjes = "regenboog"
        self.oldlampjes = None
        self.change = 0

    def on_message(self,client, userdata, msg):
        if msg.topic == "hack42/lampjesemu":
            self.lampjes = msg.payload
            if self.lampjes != self.oldlampjes:
                self.change = 1

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]


    def run(self):
         self.client = client = paho.Client()
         self.client.on_message = self.on_message
         self.client.connect("192.168.142.66", 1883, 60)
         self.client.subscribe("hack42/lampjesemu")
         self.client.subscribe("hack42/sidedoor/doorbell")
         self.client.loop_start()
         self.lampjes = "regenboog" 
         while True:
             try:
                 themod = getattr(mods, self.lampjes)
                 thefunc = getattr(themod, 'run')
                 for (tijd, data) in thefunc():
                     x = 0 
                     if self.change == 1:
                         break;
                     if x % 5 == 0:
                         self.client.publish("loungeledemu/data",base64.b64encode(data))
                         time.sleep(tijd*5 if tijd>0.04 else 5)
                         if self.change == 1:
                             break
                     x += 1
                 if self.change == 1:
                   print "Switching"
                   self.change = 0
                 else: 
                   self.lampjes = "regenboog"
             except:
                 import traceback
                 print traceback.format_exc()
                 self.lampjes = "regenboog"


leds = RunLeds()
leds.run()
