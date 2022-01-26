
#!/bin/bash
set -x

api_key="..."
i="1"
while [ $i -lt 252 ]
do
    echo $i
    curl -H "Authorization: Bearer "${api_key}" -X GET "https://api.list.co.uk/v1/events?page="${i} >> events_1_252.json
    i=$[$i+1]
done

