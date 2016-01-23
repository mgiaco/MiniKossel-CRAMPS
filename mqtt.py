#!/usr/bin/env python

import linuxcnc
import paho.mqtt.publish as mqtt
from retrying import retry


try:
    s = linuxcnc.stat() 
    s.poll()
except linuxcnc.error, detail:
    print "error", detail
    sys.exit(1)

channel = '/3dprinter/delta/'
broker = '192.168.88.104'
port = '1883'

@retry(wait_fixed=5000)
def publish():
    mqtt.single(channel + 'ain2', s.ain[2], hostname=broker, port=port)
    print "ok"

publish()
