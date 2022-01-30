#!/bin/bash
set -x

api_key="INSERT YOUR KEY"
i="1"
NUM="10"
while [ $i -lt $NUM ]
do
    echo $i
    i=$[$i+1]
    curl -H "Authorization: Bearer ${api_key}"  -X GET "https://api.list.co.uk/v1/places?page="${i} >> places.json
done

