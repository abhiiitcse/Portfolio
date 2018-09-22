#!/usr/bin/env bash

ROOT_PATH=`pwd`

# shut down uwsgi
uwsgi --stop $ROOT_PATH/mysite.pid
#remove sock files
rm $ROOT_PATH/mysite.sock
rm $ROOT_PATH/mysite.pid
# gracefully stop nginx
sudo nginx -s quit