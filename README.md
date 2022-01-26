# Exploring_TheList_Data


This repo has a collection of scripts, and notebooks for mining [The LIST](https://api.list.co.uk/). The API serves two main types of **data events and places**. 
Here we can find facilities for: 
- Downloading LIST events & places to json files
- Upload events & places json files to an ElasticSearch
- Explore and Analyse Events - Mining Events data - Using Pandas DataFrames & Deep Learning Transformers.  

For visualizing the "Anlyasing_Events" we recommend to use the [nbviewer](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/Analysing_Events.ipynb), since it has several images created with plotly. 

For downlading data from the [LIST API](https://api.list.co.uk/getting-started), it is necessary to register and get an API KEY.

Events and places data are downloaded as a collection of documents. Having a document (which is a dictionary) per event and per place.
Bellow we have as an example, a place document and event document. 

<img width="1098" alt="place_document" src="https://user-images.githubusercontent.com/6940078/151236352-38e9af2b-0e4b-45ba-9391-b287a2126879.png">

<img width="1121" alt="event_document" src="https://user-images.githubusercontent.com/6940078/151236355-10037e7b-ab12-436b-b2db-17b8642ba71e.png">

The events and places fully documented in this [link](https://api.list.co.uk/documentation). 

A representation of events information can be visualized bellow

<img width="1121" alt="events_classes" src="./events_classes.png">

<img width="1121" alt="places_classes" src="./places_classes.png">


