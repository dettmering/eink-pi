#!/bin/sh

python3 generate-svg.py
rsvg-convert --background-color=white -o screen-output.bmp screen-template.svg
python3 draw.py screen-output.bmp
rm screen-output.*
