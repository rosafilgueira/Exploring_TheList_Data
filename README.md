# Exploring_TheList_Data


This repo has a collection of scripts, and notebooks for mining [The LIST](https://api.list.co.uk/). The API serves two main types of **data events and places**. 
Here we can find facilities for: 
- Downloading LIST events & places to json files
- Upload events & places json files to ElasticSearch
- Explore and Analyse Events - Mining Events - Using Pandas DataFrames & Deep Learning Transformers.  
- Explore and Analyse Places - Mining Places - Using Pandas DataFrames & Deep Learning Transformers.  

## 1. Visualizing Analyses Notebooks
**IMPORTANT** For visualizing the "Analysing_Events/Places" notebooks we recommend to click here:
  - [nbviewer_events](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/Analysing_Events.ipynb), since it has several images created with plotly. 
  - [nbviewer_places](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/Analysing_Places.ipynb), since it has several images created with plotly. 

## 2. Downloading Events and Places Sample Dataset

For downlading data from the [LIST API](https://api.list.co.uk/getting-started), it is necessary to register and get an API KEY.
Once you have that, you can modify "download_events.sh" and "download_places.sh" bash scripts to insert your api_key, and run them:

```
./download_events.sh
./download_place.sh
```
Data (events and places) will be downloaded in json format. 

## 3. Events and Places Features

Events and places data are downloaded as a collection of documents, having a document (which is a dictionary) per event and per place.
Bellow we have as an example, a place document and event document. 

- **Events**: 
   <img width="1098" alt="place_document" src="https://user-images.githubusercontent.com/6940078/151236352-38e9af2b-0e4b-45ba-9391-b287a2126879.png">

- **Places**:
   <img width="1121" alt="event_document" src="https://user-images.githubusercontent.com/6940078/151236355-10037e7b-ab12-436b-b2db-17b8642ba71e.png">

The **events and places metadata** are fully documented in this [link](https://api.list.co.uk/documentation). 

A representation of **events** information can be visualized bellow

<img width="1121" alt="events_classes" src="./events_classes.png">

A representation of **places** information can be visualized bellow

<img width="1121" alt="places_classes" src="./places_classes.png"3>

## 4. Running Analyses Notebooks locally

In order to run the Analysing_Events and Analysing_Places notebooks locally, you need to download events and places data first (see section 2), and store them in **events.json** and **places.json** files.

## 5. Loading Data to ElasticSearch

Download events and places data (see Section 2), open two terminals and follow the next steps:

- **Terminal 1)**
  1. Download [elasticsearch-7.16.3](https://www.elastic.co/downloads/elasticsearch)
  2. Decompress the elasticsearch-7.16.3 folder
  3. cd elasticsearch-7.16.3/
  4. ./bin/elasticsearch 
  (Let it running - do not close this terminal)

- **Terminal  2)**
   1. python create_load_indexes_ES.py  —> It creates two ES indexes (events and places) and loads the json files (events.json and places.json) into Elastic Search. 
   2. ``` curl 'localhost:9200/_cat/indices?v’ ``` —> It checks that the indexes and data have been created correctly in ElasticSearch


