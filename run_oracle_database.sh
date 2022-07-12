#!/bin/bash
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
