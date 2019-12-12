from simple import MQTTClient
import time
import network
import neopixel,machine
import socket
port = 4242
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0',port))
s.settimeout(0)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# config je wifi ff
# sta_if.connect('BeContinue','<HIERMOETEENWACHTWOORDJA>')
time.sleep(10)
pin = machine.Pin(4)
np = neopixel.NeoPixel(pin,1000)


def sub_cb(topic, msg):
  global np
  start = msg[0] * 256 + msg[1]
  if start == 0xFFFF:
      np.write()
      return
  msg = msg[2:]
  np.buf[start:start + len(msg)] = msg
  return
   
client_id = "lampjes"
mqtt_server = "192.168.142.66"
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_last_will(topic='hack43/tele/loungeledjes/status',msg='offline',retain=True)
  client.connect()
  client.publish('hack42/tele/loungeledjes/ifconfig', str(sta_if.ifconfig() ), retain = True)
  client.publish('hack42/tele/loungeledjes/status','online',retain = True)
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    try:
        data,addr=s.recvfrom(1500)
        if len(data)>2:
            sub_cb('lampjes',data)
    except:
        pass
  except OSError as e:
    restart_and_reconnect()
