#!/bin/bash

CONTAINER_ID="97179d2b91d4"

docker start $CONTAINER_ID

docker exec $CONTAINER_ID mkdir -p /home/doc-bd-a1/result

docker exec $CONTAINER_ID bash -c 'if compgen -G "/home/doc-bd-a1/service-result/*.csv" > /dev/null; then cp /home/doc-bd-a1/service-result/*.csv /home/doc-bd-a1/result/; else echo "No CSV files found."; fi'

docker exec $CONTAINER_ID bash -c 'if compgen -G "/home/doc-bd-a1/service-result/*.txt" > /dev/null; then cp /home/doc-bd-a1/service-result/*.txt /home/doc-bd-a1/result/; else echo "No TXT files found."; fi'

docker exec $CONTAINER_ID bash -c 'if [ -f /home/doc-bd-a1/service-result/vis.png ]; then cp /home/doc-bd-a1/service-result/vis.png /home/doc-bd-a1/result/; else echo "No PNG file found."; fi'

docker exec $CONTAINER_ID bash -c 'if [ -f /home/doc-bd-a1/service-result/k.txt ]; then cp /home/doc-bd-a1/service-result/k.txt /home/doc-bd-a1/result/; else echo "No k.txt file found."; fi'

docker exec $CONTAINER_ID bash -c 'if [ "$(ls -A /home/doc-bd-a1/result)" ]; then echo "Files are in the result directory."; else echo "Error: Result directory is empty."; fi'

docker cp $CONTAINER_ID:/home/doc-bd-a1/result/. "C:\\bd-a1\\service-result/"

docker stop $CONTAINER_ID
