#!/usr/bin/python3
# -*- coding:utf-8 -*-

import epd2in7
from PIL import Image,ImageDraw,ImageFont
import sys

def draw(imgfile):
    epd = epd2in7.EPD()
    epd.init()
    epd.Clear(0xFF)
    
    Himage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 255: clear the frame
    
    Himage = Image.open(imgfile)
    epd.display(epd.getbuffer(Himage))
        
    epd.sleep()

if __name__ == '__main__':
    draw(sys.argv[1])
