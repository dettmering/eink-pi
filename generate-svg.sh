#!/bin/sh

python3 generate-svg.py
rsvg-convert --background-color=white -o screen-output.png screen-template.svg
