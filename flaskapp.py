#!/usr/local/bin/python
# coding: latin-1

#import requried modules

from flask import Flask, request, jsonify
from ip2geotools.databases.noncommercial import DbIpCity
    
app = Flask('flaskapp')

# Decorator defines a route
# http://localhost:5000/

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
    response = DbIpCity.get(ip, api_key='free')
    lat = response.latitude
    long = response.longitude
    
    #print the vars for self testing
    print(response.latitude)
    print(response.longitude)
    print ("the type is", type)
    print ("the product name is", product)
    print ("the usage is", usage)
    print ("the price is", price)
    print ("the currency is", currency)

    
#convert data to JSON format
    jsonobj =  jsonify(type=type,
                   product=product,
                   usage=usage,
                   price=price,
                   currency=currency,
                   origin_ip=request.remote_addr,
                   latitude_location=lat,
                   longitude_location=long
                   )
    
    return jsonobj
     
if __name__ == '__main__':
    app.run(host='0.0.0.0')   
        

