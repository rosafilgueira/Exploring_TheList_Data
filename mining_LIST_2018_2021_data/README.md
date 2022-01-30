## 1. Visualizing Analyses Notebooks
For visualizing the "Analysing_Events/Places" notebooks we recommend to click here:
  - events:
	- [2018_events](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/html_visualizations/Analysing_Events_sample_20180501.html?flush_cache=true) since it has several dynamic visualizations
	- [2019_events](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/html_visualizations/Analysing_Events_sample_20190501.html?flush_cache=true) since it has several dynamic visualizations
	- [2020_events](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/html_visualizations/Analysing_Events_sample_20200501.html?flush_cache=true) since it has several dynamic visualizations
	- [2021_events](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/html_visualizations/Analysing_Events_sample_20210501.html?flush_cache=true) since it has several dynamic visualizations

  - places:
       [2018_places](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/html_visualizations/Analysing_Places_sample_20180501.html?flush_cache=true) since it has several dynamic visualizations


## 3. Events and Places Features

Events and places data are a collection of documents. We have a document (which is a dictionary) per event and per place.
Bellow we have two examples, one for an event document and another for a place document. 

- **Events**: 

- **Places**:


A representation of **events** information is visualised  bellow:

<img width="1121" alt="events_classes" src="./events_classes.png">

A representation of **places** information is visualised bellow:

<img width="1121" alt="places_classes" src="./places_classes.png">

## 4. Running Analyses Notebooks locally

In order to run "Analysing_Events" and "Analysing_Places" notebooks, you need to download events and places data first (see section 2), and store them in **events.json** and **places.json** files.

## 5. Loading Data to ElasticSearch

Data can be also stored in ElasticSearch. Once you have your data downloaded (see Section 2) open two terminals and follow the next steps:
- **Terminal 1)**
  1. Download [elasticsearch-7.16.3](https://www.elastic.co/downloads/elasticsearch)
  2. Decompress the elasticsearch-7.16.3 folder
  3. cd elasticsearch-7.16.3/
  4. ./bin/elasticsearch 
  (Let it running - do not close this terminal)

- **Terminal  2)**
   1. python create_load_indexes_ES.py  —> It creates two ES indexes (events and places) and loads the json files (events.json and places.json) into Elastic Search. 
   2. ``` curl 'localhost:9200/_cat/indices?v’ ``` —> It checks that the indexes and data have been created correctly in ElasticSearch (ES).

At the end of these steps you will events and data stored in your ElasticSearch. You can visualise this data (once is in ES) automatically also using Kibana. 

