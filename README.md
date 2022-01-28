# Exploring_TheList_Data


This repo has a collection of scripts, and notebooks for mining [The LIST](https://api.list.co.uk/). The API serves two main types of **data events and places**. 

Here we can find facilities for: 
- Downloading LIST events & places to json files
- Uploading events & places json files to ElasticSearch
- Exploring and Analysing Events - Mining Events - Using Pandas DataFrames & Deep Learning Transformers.  
- Exploring and Analysing Places - Mining Places - Using Pandas DataFrames & Deep Learning Transformers.  

## 0. Preparations

We recommend to install the requirements specified in requirements.txt for sections 2 to 5.
And also to have Python 3.7+ enviroment. 

```
pip install -r requirements.txt 

```
## 1. Visualizing Analyses Notebooks
For visualizing the "Analysing_Events/Places" notebooks we recommend to click here:
  - [events](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/html_visualizations/Analysing_Events_sample_20180501.html?flush_cache=true) since it has several dynamic visualizations
  - [places](https://nbviewer.org/github/rosafilgueira/Exploring_TheList_Data/blob/main/html_visualizations/Analysing_Places_sample_20180501.html?flush_cache=true) since it has several dynamic visualizations

## 2. Downloading Events and Places Sample Dataset

For downlading data from the [LIST API](https://api.list.co.uk/getting-started), it is necessary to register and get an API KEY.
Once you have your API KEY, modify "download_events.sh" and "download_places.sh" scripts and run them:

```
./download_events.sh
./download_place.sh
```
These will download data (events and places) in two files (json format):
- events.json
- places.json 

**Note**: The [LIST_API notebook](./LIST_API.ipynb) has aditional information that can be useful for this step. 

## 3. Events and Places Features

Events and places data are a collection of documents. We have a document (which is a dictionary) per event and per place.
Bellow we have two examples, one for an event document and another for a place document. 

- **Events**: 
   <img width="1098" alt="place_document" src="https://user-images.githubusercontent.com/6940078/151236352-38e9af2b-0e4b-45ba-9391-b287a2126879.png">

- **Places**:
   <img width="1121" alt="event_document" src="https://user-images.githubusercontent.com/6940078/151236355-10037e7b-ab12-436b-b2db-17b8642ba71e.png">

The **events and places metadata** are fully documented in this [link](https://api.list.co.uk/documentation). 

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

**Note**: The [LIST_API notebook](./LIST_API.ipynb) has aditional information that can be useful for this step.
