#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd2in7.EPD()
    epd.init()
    epd.Clear(0xFF)
    
    Himage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 255: clear the frame
    
    print("read bmp file")
    Himage = Image.open('2in7.bmp')
    epd.display(epd.getbuffer(Himage))
        
    epd.sleep()
        
except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()

