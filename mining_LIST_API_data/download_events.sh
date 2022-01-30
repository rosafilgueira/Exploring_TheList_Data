#!/bin/bash
set -x

api_key="INSERT YOUR KEY"
i="1"
NUM="10"
while [ $i -lt $NUM ]
do
    echo $i
    curl -H "Authorization: Bearer ${api_key}"  -X GET "https://api.list.co.uk/v1/events?page="${i} >> events.json
    i=$[$i+1]
done

