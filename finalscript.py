#!/usr/bin/env python3

import board
import neopixel
from time import sleep

LEDcount = 8

pixels = neopixel.NeoPixel(board.D18, LEDcount)

while True:
  pixels.fill((0,0,150))
  sleep(0.2)
  pixels.fill((0,0,130))
  sleep(0.2)
  pixels.fill((0,0,110))
  sleep(0.2)
  pixels.fill((0,0,90))
  sleep(0.2)
  pixels.fill((0,0,70))
  sleep(0.2)
  pixels.fill((0,0,50))
  sleep(0.2)
  pixels.fill((0,0,70))
  sleep(0.2)
  pixels.fill((0,0,90))
  sleep(0.2)
  pixels.fill((0,0,110))
  sleep(0.2)
  pixels.fill((0,0,130))
  sleep(0.2)

