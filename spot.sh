#!/bin/bash
realpath() {
  [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

CURR_DIR=$( realpath "$0" | sed 's|\(.*\)/.*|\1|')
python3 $CURR_DIR/spot.py "$@"
