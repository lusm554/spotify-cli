#!/bin/bash
chmod +x spot.sh
ln -s $PWD/main.py /usr/local/bin/spot.py
sudo cp spot.sh /usr/local/bin/spot
export SPOT_TOKEN_PATH="$PWD/.env"
