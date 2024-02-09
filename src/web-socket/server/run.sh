#!/bin/bash

if [ $USE_DEV_MODE = "true" ];
  then nodemon --exec python -u main.py $WEB_SOCKET_SERVER_PORT;
  else python -u main.py $WEB_SOCKET_SERVER_PORT;
fi