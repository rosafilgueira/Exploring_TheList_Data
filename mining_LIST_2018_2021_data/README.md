## 1. Visualizing Analyses Notebooks
For visualizing the "Analysing_Events/Places" notebooks we recommend to click here:

We have several HTML visualizations for our notebooks - so you can see the analyses performed without running them. 


 - case study[**NEW!!**]:  
       -[case study using sample dataset from Nov 2017 to 2022](https://storage.googleapis.com/case_study_list/Case_Study_v2.html): In this case study with have analysed together all the sample events available from 2017 to 2022. These are our **preliminar** results. In this case study, we can see how the number of events, schedules, performances have drastically changed over the last 5 years.  

     
  - events:
	- [2017_sample_events](https://storage.googleapis.com/case_study_list/Analysing_Events_sample_20171101.html) 
	- [2018_sample_events](https://storage.googleapis.com/case_study_list/Analysing_Events_sample_20180501.html) 
	- [2019_sample_events](https://storage.googleapis.com/case_study_list/Analysing_Events_sample_20190501.html) 
	- [2020_sample_events](https://storage.googleapis.com/case_study_list/Analysing_Events_sample__20200501.html) 
	- [2021_sample_events](https://storage.googleapis.com/case_study_list/Analysing_Events_sample_sample_20210501.html) 
  - places:
	- [2017_sample_places](https://storage.googleapis.com/case_study_list/Analysing_Places_sample_20171101.html) 
	- [2018_sample_places](https://storage.googleapis.com/case_study_list/Analysing_Places_sample_20180501.html) 
	- [2019_sample_places](https://storage.googleapis.com/case_study_list/Analysing_Places_sample_20190501.html) 
	- [2020_sample_places](https://storage.googleapis.com/case_study_list/Analysing_Places_sample_20100501.html) 
	- [2021_sample_places](https://storage.googleapis.com/case_study_list/Analysing_Places_sample_20210501.html) 


## 2. Events and Places Features

Events and places data are a collection of documents. We have a document (which is a dictionary) per event and per place.
Bellow we have two examples, one for an event document and another for a place document. 

- **Events**: 

- **Places**:


A representation of **events** information is visualised  bellow:

<img width="1121" alt="events_classes" src="./events_classes.png">

A representation of **places** information is visualised bellow:

<img width="1121" alt="places_classes" src="./places_classes.png">

## 3. Running Analyses Notebooks locally

You need access to sample dataset 

## 4. Loading Data to ElasticSearch

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

