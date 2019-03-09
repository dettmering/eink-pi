#!/usr/bin/python3

# Kindle Weather Display
# Matthew Petroff (http://mpetroff.net/)
# September 2012

from xml.dom import minidom
import datetime
import codecs

#
# Preprocess SVG
#

# Open SVG to process
output = codecs.open('screen-template.svg', 'r', encoding='utf-8').read()

# Insert icons and temperatures
#output = output.replace('LOW_ONE',str(lows[0])).replace('LOW_TWO',str(lows[1])).replace('LOW_THREE',str(lows[2])).replace('LOW_FOUR',str(lows[3]))

# Write output
codecs.open('screen-output.svg', 'w', encoding='utf-8').write(output)
