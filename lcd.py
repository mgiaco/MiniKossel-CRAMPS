#!/usr/bin/env python

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageDraw, ImageFont

import linuxcnc

device = ssd1306(port=1, address=0x3C)

s = linuxcnc.stat()

font = ImageFont.load_default()
font2 = ImageFont.truetype('fonts/Volter__28Goldfish_29.ttf', 20)

while 1:
    s.poll()
    with canvas(device) as draw:
        draw.text((0, 0), "E0: %s C" % str(s.ain[2]), font=font2, fill=255)
        draw.text((0, 20), "Z: %s mm" % str(round(s.actual_position[2],2)), font=font2, fill=255)




#while 1:
#  s.poll()
#  lcd.lcd_display_string("%s %s C" % ('E0:', str(s.ain[2])), 1)
#  lcd.lcd_display_string("%s %s mm" % ('Z:', str(round(s.actual_position[2],2))), 2)
#  sleep(1)

