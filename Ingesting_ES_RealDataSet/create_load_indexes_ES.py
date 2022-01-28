import json
import configparser
import os
from os import listdir
from os.path import isfile, join

from tqdm import tqdm

from elasticsearch import Elasticsearch, helpers
import os, uuid

#####
#NOTE: I had to modify the json files to rename some fields- problems with fields with more than 2 dots
#- "place.facilities.toilets.disabled" --> "place.facilities.toilets.disabled"
#- "place.facilities.toilets_baby.changing --> "place.facilities.toilets_baby-changing"
####

mapping_places = {
    "mappings": {
      "properties": {
        "address": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "country_code": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "created_ts": {
          "type": "date"
        },
        "descriptions": {
          "properties": {
            "description": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "type": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "email": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "loc": {
          "properties": {
            "latitude": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "longitude": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "modified_ts": {
          "type": "date"
        },
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "phone_numbers": {
          "properties": {
            "box_office": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "info": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "place_id": {
          "type": "long"
        },
        "postal_code": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "properties": {
          "properties": {
            "place": {
              "properties": {
                "capacity": {
                  "properties": {
                    "max": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    }
                  }
                },
                "child-friendly": {
                  "type": "boolean"
                },
                "child-restrictions": {
                  "type": "boolean"
                },
                "facilities": {
                  "properties": {
                    "dogs-allowed": {
                      "type": "boolean"
                    },
                    "free-wifi": {
                      "type": "boolean"
                    },
                    "guide-dogs": {
                      "type": "boolean"
                    },
                    "hearing-loop": {
                      "type": "boolean"
                    },
                    "parking": {
                      "type": "boolean"
                    },
                    "toilets": {
                      "type": "boolean"
                    },
                    "toilets_baby-changing": {
                      "type": "boolean"
                    },
                    "toilets_disabled": {
                      "type": "boolean"
                    },
                    "wheelchair-access": {
                      "type": "boolean"
                    }
                  }
                }
              }
            }
          }
        },
        "sort_name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "status": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "tags": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "town": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "website": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        }
      }
    }
}



mapping_events = {
    "mappings": {
        "properties": {
          "alternative_names": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "category": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "created_ts": {
          "type": "date"
        },
        "descriptions": {
          "properties": {
            "description": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "type": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "event_id": {
          "type": "long"
        },
        "id": {
          "type": "long"
        },
        "modified_ts": {
          "type": "date"
        },
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "phone_numbers": {
          "properties": {
            "box_office": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "info": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "properties": {
          "properties": {
            "actor": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "actor:sample": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "affiliate:getmein": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "affiliate:seatwave": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "author": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "awards:fringe-sustainable-practice:2015": {
              "type": "boolean"
            },
            "booking_essential": {
              "type": "boolean"
            },
            "cast": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "director": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "dropin_event": {
              "type": "boolean"
            },
            "event:demographic": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "event:language": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "expected_visit_duration": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:amg_id": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:certificate": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:certificate:bbfc": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:colour": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:country-of-origin": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:imdb": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:imdb_id": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:itunes": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:metacritic": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:metcritic": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:mojo_id": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:release-date:uk": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:rotten-tomatoes": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:rotten_tomatoes_id": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:running-time": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:subtitle": {
              "type": "boolean"
            },
            "film:wikipedia": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:wikipedia:image": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:wikipedia:image_caption": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "film:year": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "list:feed:imageid": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "list:importance": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "list:importanceOverride": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "list:website:comments-enabled": {
              "type": "boolean"
            },
            "list:website:comments-end-date": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "list:website:company": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "list:website:hitlisted": {
              "type": "boolean"
            },
            "list:website:list-of-sites": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "organisation": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "pa:rating": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "place:capacity:max": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "simpleview:original:categories": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "writer": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "ranking_in_level": {
          "type": "long"
        },
        "ranking_level": {
          "type": "long"
        },
        "schedules": {
          "properties": {
            "end_ts": {
              "type": "date"
            },
            "performance_space": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "performances": {
              "properties": {
                "descriptions": {
                  "properties": {
                    "description": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    },
                    "type": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    }
                  }
                },
                "duration": {
                  "type": "long"
                },
                "links": {
                  "properties": {
                    "type": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    },
                    "url": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    }
                  }
                },
                "properties": {
                  "properties": {
                    "event": {
                      "properties": {
                        "festival": {
                          "type": "text",
                          "fields": {
                            "keyword": {
                              "type": "keyword",
                              "ignore_above": 256
                            }
                          }
                        },
                        "film": {
                          "properties": {
                            "3d": {
                              "type": "boolean"
                            },
                            "autism-friendly": {
                              "type": "boolean"
                            },
                            "imax": {
                              "type": "boolean"
                            },
                            "over-18s": {
                              "type": "boolean"
                            },
                            "parent-and-baby": {
                              "type": "boolean"
                            },
                            "premium-screening": {
                              "type": "boolean"
                            },
                            "senior": {
                              "type": "boolean"
                            },
                            "subtitled": {
                              "type": "boolean"
                            }
                          }
                        },
                        "minimum-age": {
                          "type": "text",
                          "fields": {
                            "keyword": {
                              "type": "keyword",
                              "ignore_above": 256
                            }
                          }
                        },
                        "session": {
                          "type": "text",
                          "fields": {
                            "keyword": {
                              "type": "keyword",
                              "ignore_above": 256
                            }
                          }
                        },
                        "support": {
                          "type": "text",
                          "fields": {
                            "keyword": {
                              "type": "keyword",
                              "ignore_above": 256
                            }
                          }
                        },
                        "theatre": {
                          "properties": {
                            "bsl-interpreted": {
                              "type": "boolean"
                            },
                            "captioned": {
                              "type": "boolean"
                            }
                          }
                        }
                      }
                    },
                    "list": {
                      "properties": {
                        "hitlisted": {
                          "type": "boolean"
                        }
                      }
                    },
                    "performance": {
                      "properties": {
                        "cancelled": {
                          "type": "boolean"
                        },
                        "sold-out": {
                          "type": "boolean"
                        }
                      }
                    }
                  }
                },
                "tickets": {
                  "properties": {
                    "currency": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    },
                    "description": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    },
                    "max_price": {
                      "type": "float"
                    },
                    "min_price": {
                      "type": "long"
                    },
                    "type": {
                      "type": "text",
                      "fields": {
                        "keyword": {
                          "type": "keyword",
                          "ignore_above": 256
                        }
                      }
                    }
                  }
                },
                "time_unknown": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                },
                "ts": {
                  "type": "date"
                }
              }
            },
            "phone_numbers": {
              "properties": {
                "info": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
            },
            "place_id": {
              "type": "long"
            },
            "start_ts": {
              "type": "date"
            }
          }
        },
        "sort_name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "status": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "tags": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "website": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        }
      }
    }
  }

'''
generator to push bulk data from a JSON
file into an Elasticsearch index
'''
def bulk_json_data(json_list, _index, doc_type):
    for num, doc in enumerate(json_list):
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
    dataset="../dataset/"
    jsonfiles = [f for f in listdir(dataset) if isfile(join(dataset, f))]
    print(jsonfiles)
    es = Elasticsearch()

    ## drop and create index for expertise
    print("Deleting-Creating-Loading Places to ES")
    es.indices.delete(index=index_name_places, ignore=[400, 404])
    es.indices.create(index=index_name_places, body=mapping_places, ignore=400)
    print("Deleting-Creating-Loading Events to ES")
    es.indices.delete(index=index_name_events, ignore=[400, 404])
    es.indices.create(index=index_name_events, body=mapping_events, ignore=400)
    
    for i in jsonfiles:
        print("Uploading dataset %s" %i) 
        with open(dataset+"/"+i, 'r') as f:
            data = json.load(f)
        places=data["places"]
        events=data["events"]
     
        #### remove dots

        print(len(events))
        response = helpers.bulk(es, bulk_json_data(places, index_name_places , "_doc"))
        print ("\nRESPONSE %s - PLACE:%s" %(response, i))

        print("--------")
        response = helpers.bulk(es, bulk_json_data(events, index_name_events , "_doc"))
        print ("\nRESPONSE %s - EVENT:%s" %(response, i))
