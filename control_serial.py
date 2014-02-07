#!/usr/bin/python

import serial
import pygame

ser = serial.Serial("/dev/ttyUSB0", 9600);

screen = pygame.display.set_mode([300,300]);

last = ""

pygame.init()
while True:
  event = pygame.event.poll()
  if event.type == pygame.KEYDOWN:
    if event.key == last: continue
    elif event.key == pygame.K_w:
      last = pygame.K_w
      ser.write("1")
    elif event.key == pygame.K_a:
      last = pygame.K_a
      ser.write("8")
    elif event.key == pygame.K_d:
      last = pygame.K_d
      ser.write("4")
    elif event.key == pygame.K_s:
      last = pygame.K_s
      ser.write("2")
    print last
  elif event.type == pygame.KEYUP:
    last = ""
    ser.write("0");
