
#import requried modules

from flask import Flask, request, jsonify
from ip2geotools.databases.noncommercial import DbIpCity
from datetime import datetime, date, time, timezone
from elasticsearch import Elasticsearch
import json


    
app = Flask('flaskapp')

#set the proper GET endpoint
@app.route('/tracking', methods=["GET"])

def index(type="", product="", usage="", price="", currency="" ):
    
#receive the URL PARAMS
    type = request.args.get('type', type)    
    product = request.args.get('product', product)    
    usage = request.args.get('usage', usage)    
    price = request.args.get('price', price)    
    currency = request.args.get('currency', currency)
    ip = request.remote_addr    
    
    #return error when coming from private ip
    try:
        response = DbIpCity.get(ip, api_key='free')    
    except Exception:
        return('oops, cannot find your location, are you coming from a public IP?')
    
    #convert lat and long to variables
    lat = response.latitude
    long = response.longitude
    location ="{0},{1}".format(lat, long)

    #convert data to JSON format
    json_element={}
    json_element['product']=product
    json_element['usage']=usage
    json_element['price']=price
    json_element['currency']=currency
    json_element['ip']=ip
    json_element['lat']=lat
    json_element['lon']=long
    json_element['timestamp']=datetime.utcnow()
    json_element['location']=location
    
    

    #set ElasticSearch host
    client = Elasticsearch(hosts=["http://elasticsearch:9200"])
      
    
    #send the json to elastic using Elastic python module
    response = client.index(
        index = 'my_index',
        doc_type = '_doc',
        body = json_element
       )
    
    return json_element
     
if __name__ == '__main__':
    app.run(host='0.0.0.0') 
