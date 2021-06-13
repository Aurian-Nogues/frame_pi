#!/bin/bash

# commands to prevent screen sleeping
sudo xset s off
sudo xset -dpms
sudo xset s noblank

# commands to start and continue running simultaneously display manager and bluetooth receiver
/home/pi/frame_pi/venv/bin/python3 /home/pi/frame_pi/display/display_manager.py &
sudo /home/pi/frame_pi/venv/bin/python3 /home/pi/frame_pi/main.py
