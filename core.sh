#!/bin/bash
while true
do
    sudo fuser -k 7676/tcp
    python3 core.py
done
