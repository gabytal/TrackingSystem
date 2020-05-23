# TrackingSystem
This is a tracking system, based on Python api with Flask framework.
It basically takes url parameters from the user, builds a JSON from it,
takes the origin IP of the requester, converts it to Lat & Long location format,
then sends it to elastic search with python Elasticsearch module:

Here is the configuration for creating a new index in elastic search:

#create an index called "my_index" with the right properties:

```JSON
PUT my_index
{
    "settings" : {
        "index" : {
            "number_of_shards" : 1, 
            "number_of_replicas" : 0
        }
    },
  "mappings": {
    "properties": {
      "location": {"type": "geo_point"},
       "product" : { "type" : "text" },
        "usage" : { "type" : "text" },
          "price" : { "type" : "text" },
            "currency" : { "type" : "text" },
              "ip" : { "type" : "text" },
                  "timestamp" : { "type" : "date" }
    }
  }
}

```
Docker-Compose details:

  | SERVICE | CONTAINER PORT | HOST PORT |
  | ------------- | ------------- | ----- |
  | Python API  | 5000   | 5000 |
  | Kibana  | 5601 | 5601 |
  | Elastic Search | 9200, 9300 | 9200, 9300 |
