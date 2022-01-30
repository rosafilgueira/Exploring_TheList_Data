# Exploring The List Data 2018-2021

This repo has a collection of scripts, notebooks and HTML visualizations for mining The LIST data. The LIST serves two main types of data: **events and places**. 

We have two types of mining resources: one for the **general public** (*mining_LIST_API_data directory*) and another one for users which have access to **datasets from 2018 to 2021** (*mining_LIST_2018_2021 directory*).

The reason for which we have separated them is because data (events and places) downloaded from the LIST API is slightly different (in terms of schema) than the one obtained directly from the LIST. 

Nevertheless, we have included in both directories results from our preliminary analyses in HTML format. 

## General Public

This collection of resources are intended for anyone who has previously registered to the [The LIST API](https://api.list.co.uk/), and wants to explore the downloaded through the API.

Go to [mining_LIST_API_data](./mining_LIST_API_data) for starting mining this type of resource.

Note: A FREE account is limited to 1,000 requests per month.

## LIST Dataset 2018 to 2021

This collection of resources are intended for users with access to LIST dataset from **2018 to 2021**. Therefore, only users with access to this dataset will be able to run the notebooks locally. However, the results of our primilary analyses area available in HTML format.  

Go to [mining_LIST_2018_2021_data](./mining_LIST_2018_2021_data) for starting mining this type of resource. 

Note: **The dataset used in this directory is not available in this repository**. 


## Preparations

Indepedently of the type of resource to mine, we recommend to install the requirements specified in requirements.txt for sections 2 to 5.
And also to have Python 3.7+ enviroment. 

```
pip install -r requirements.txt 

```
