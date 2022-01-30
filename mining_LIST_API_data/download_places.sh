#!/bin/bash
set -x

api_key="INSERT YOUR KEY"
i="1"

### NUM variable indicates the number of pages to download. Be carreful with this variable. Remember 1000 free downloads per month
### Each page has 100 places

NUM="10"
while [ $i -lt $NUM ]
do
    echo $i
    i=$[$i+1]
    curl -H "Authorization: Bearer ${api_key}"  -X GET "https://api.list.co.uk/v1/places?page="${i} >> places.json
done

