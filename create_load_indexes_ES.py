import json
import configparser
import os

from tqdm import tqdm

from elasticsearch import Elasticsearch, helpers
import os, uuid

mapping_places = {
    "mappings": {
        "properties": {
            "properties": {
		"place.times.seasonal": {"type": "text"},
                "place.year-opened": {"type":"text"},
                "place.the-list-card": {"type":"boolean"},
                "place.parent-company": {"type":"text"},
                "place.times.bar-open": {"type":"text"},
                "place.times.closed-days": {"type":"text"},
                "place.times.food-served": {"type":"text"},
		"place.child-restrictions": {"type": "boolean"}, 
		"place.child-restrictions_details": {"type": "text"}, 
		"place.facilities.childrens-high-chairs": {"type": "boolean"}, 
		"place.facilities.parking": {"type": "boolean"}, 
      		"place.facilities.toilets":  {"type": "boolean"}, 
      		"place.facilities.free-wifi":  {"type": "boolean"}, 
      		"place.facilities.dogs-allowed":  {"type": "boolean"}, 
                "place.facilities.wheelchair-access": {"type": "boolean"},
                "place.facilities.toilets_disabled": {"type": "boolean"},
                "phone.info": {"type": "text"},
                "phone.box-office": {"type": "text"},
		}
	    }, 
            "place_id": {"type": "keyword"},
            "list_id": {"type": "number"},
            "created_ts" : {"type": "date", "format": "date_optional_time"},
            "modified_ts" : {"type": "date", "format": "date_optional_time"},
            "name": {"type": "text"},
            "sort_name": {"type": "text"},
            "address": {"type": "text"},
            "town": {"type": "text"},
            "postal_code": {"type": "text"},
            "country_code": {"type": "text"},
            "lat": {"type": "number"},
            "lng": {"type": "number"},
            "website": {"type": "text"},
            "tags": {"type": "text"},
            "links": {
		"properties": {
            		"url": {"type": "keyword"},
            		"title": {"type": "text"}
			}
		     },
            "descriptions": {
		"properties": {
            		"type": {"type": "text"},
            		"description": {"type": "text"}
			}
		     },
	    "images": {
		   "properties": {
            		"url": {"type": "keyword"},
            		"width": {"type": "number"},
            		"height": {"type": "number"},
            		"alt_text": {"type": "text"}
                         }
                   }
          
            }
        }
    

mapping_events = {
    "mappings": {
        "properties": {
            "event_id": {"type": "keyword"},
            "list_id": {"type": "number"},
            "created_ts" : {"type": "date"},
            "modified_ts" : {"type": "date"},
            "name": {"type": "text"},
            "sort_name": {"type": "text"},
            "website": {"type": "text"},
            "tags": {"type": "text"},
            "links": {
		"properties": {
            		"url": {"type": "keyword"},
            		"title": {"type": "text"}
			}
		     },
            "descriptions": {
		"properties": {
            		"type": {"type": "text"},
            		"description": {"type": "text"}
			}
		     },
            "properties": { 
                "phone.info": {"type": "text"},
                "phone.box-office": {"type": "text"},
                "film.imdb": {"type": "text"},
                "film.year": {"type": "text"},
                "film.running-time": {"type": "text"},
                "film.certificate": {"type": "text"},
                "film.release-date-uk": {"type": "text"},
                "film.country-of-origin": {"type": "text"},
                "film.subtitle": {"type": "boolean"},
                "event.language": {"type": "text"},
                "cast": {"type": "text"},
                "director": {"type": "text"},
                "writer": {"type": "text"}
                        },
	     "images": {
		   "properties": {
            		"url": {"type": "keyword"},
            		"width": {"type": "number"},
            		"height": {"type": "number"},
            		"alt_text": {"type": "text"}
                         }
                   },
             "schedules":{
                   "properties":{
                        "start_ts": {"type": "date"},
                        "end_ts": {"type": "date"},
                        "place_id": {"type": "keyword"},
                        "tags": {"type": "text"},
                        "ticket_summary": {"type": "text"},
                        "place": {
                           "properties":{
			    "place_id": {"type": "keyword"}, 
                            "list_id":  {"type": "keyword"},
                            "name":  {"type": "text"},
                            "address": {"type": "text"},
                            "town": {"type": "text"},
                            "postal_code": {"type": "text"},
                            "lat": {"type": "geo-point"}, 
                             "lng":{"type": "geo-point"}
                            }
                            },
                         "performances": {
                           "properties":{
                              "ts": {"type": "date"}, 
                              "duration": {"type": "number"},
                              "tickets": {
                                  "properties": {
                                  "type": {"type": "text"},
                                   "currency": {"type": "text"},
                                   "min_price": {"type": "text"},
                                   "max_price": {"type": "text"},
                                   "description": {"type": "text"}
                                  }
                                },
                                "links":{
                                   "properties": {
                                      "url": {"type": "keyword"},
                                       "title": {"type": "text"}
                                  }
                                 }

                                }
                             }
                        }
                     }
                   }
               }
        }


'''
a simple function that gets the working path of
the Python script and returns it
'''

def get_data_from_file(file_name):
    file_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_data) as f:
        data = json.load(f)
    return data


'''
generator to push bulk data from a JSON
file into an Elasticsearch index
'''
def bulk_json_data(json_file, _index, doc_type):
    json_list = get_data_from_file(json_file)
    for num, doc in enumerate(json_list):
           #print("-----")
           #print(doc)
           #print("-----")
           if '_index' not in doc:
               yield {
                    "_index": _index,
                    "_id": uuid.uuid4(),
                    "_type": doc_type,
                    "_score": "1.0",
                    "_source": doc
               }
           else:
               yield {
                    "_index": doc["_index"],
                    "_id": doc["_id"],
                    "_type": doc["_type"],
                    "_score": doc["_score"],
                    "_source": doc["_source"]
               }

if __name__ == "__main__":
    index_name_places = 'places'
    index_name_events = 'events'
    es = Elasticsearch()
    # drop and create index for expertise
    print("Deleting-Creating-Loading Places to ES")
    es.indices.delete(index=index_name_places, ignore=[400, 404])
    es.indices.create(index=index_name_places, body=mapping_places, ignore=400)
    response = helpers.bulk(es, bulk_json_data("places.json", index_name_places , "_doc"))
    print ("\nRESPONSE-PLACE:", response)

    print("Deleting-Creating-Loading Events to ES")
    es.indices.delete(index=index_name_events, ignore=[400, 404])
    es.indices.create(index=index_name_events, body=mapping_events, ignore=400)
    response = helpers.bulk(es, bulk_json_data("events.json", index_name_events , "_doc"))
    print ("\nRESPONSE-EVENTS:", response)
