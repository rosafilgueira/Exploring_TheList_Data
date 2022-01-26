
#!/bin/bash
set -x

api_key="...."
i="1"
while [ $i -lt 1000 ]
do
    echo $i
    i=$[$i+1]
    curl -H "Authorization: Bearer "${api_key}"  -X GET "https://api.list.co.uk/v1/places?page="${i} >> places_1_1000.json
done

