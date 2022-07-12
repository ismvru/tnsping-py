#!/bin/bash
# This project is libre, and licenced under the terms of the
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENCE, version 3.1,
# as published by dtf on July 2019. See the COPYING file or
# https://ph.dtf.wtf/w/wtfpl/#version-3-1 for more details.

set -ex
docker login container-registry.oracle.com
CONTAINER=$(docker run -d --rm -p 1521:1521 container-registry.oracle.com/database/express:21.3.0-xe)
echo "Started container $CONTAINER"
while [ ! "$(timeout 1s telnet localhost 1521)" ]; do
    echo "Trying again"
    sleep 1
done
echo "DB is up!"

read -n 1 -r -s -p $'Press enter to stop database and exit...\n'
docker stop "$CONTAINER"
echo "Stopped and removed container $CONTAINER"
