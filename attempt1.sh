#!/bin/bash

VIDEO_FILE=/home/hallmonitor/show_videos
COUNTDOWN_FILE=/home/hallmonitor/show_countdown

if test -f "$COUNTDOWN_FILE"; then
    echo "showing countdown"
    python3 /home/hallmonitor/countdown.py

elif test -f "$VIDEO_FILE"; then
    echo "showing videos"
    cvlc --loop -f "/home/hallmonitor/Videos/"

else
    echo "showing images"
    gthumb --slideshow "/home/hallmonitor/Pictures/"
fi
