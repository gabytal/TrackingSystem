# TrackingSystem
this is a tracking system, based on Python api with Flask.
its basically take url Parameters from the user, build a Json file from it,
take the origin IP of the requester, convert it to Lat & Long location format,
then send it to elastic search with python elasticsearch module:

here are the definition for creating a new index in elastic search:

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

