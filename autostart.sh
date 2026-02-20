#!/bin/bash
FILE=/home/hallmonitor/show_videos
if test -f "$FILE"; then
    echo "showing videos"
    cvlc --loop -f "/home/hallmonitor/Videos/"
else
    echo "showing images"
    gthumb --slideshow "/home/hallmonitor/Pictures/"
fi

