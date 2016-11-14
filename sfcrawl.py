import json
import time
import requests

'''
This is the web_crawler for SF park.
The location is San Francisco Area

@params1 is set to crawl general traffic congestion information

'''
param1 = {'lat': '37.792275', 
          'long' : '-122.397089', 
          'radius' : '10', 
          'uom' : 'mile',
          'response' : 'json',
          'pricing' : 'yes'  }


requests.adapters.DEFAULT_RETRIES = 10

#the url string for SF park
url = "http://api.sfpark.org/sfpark/rest/availabilityservice"

#counter of request numbers
i = 1

#the seat availability file

while True:
    strdate = time.strftime("%m%d%Y")
    filename_park = 'SF_'+strdate + '_park.txt'
    avalfile = open(filename_park,"a")

    seatavail = requests.get(url, params = param1)
    try:
           javal = json.loads(seatavail.text)
    except ValueError:
            continue
    else:
         if javal['STATUS'] == 'SUCCESS':
             avalfile.write(javal['AVAILABILITY_UPDATED_TIMESTAMP'] + '\n')
         for avl in javal['AVL']:
             avalfile.write(json.dumps(avl) + '\n')
             
    time.sleep(60*5)
    i = i + 1
    #if i > 600:
        #break
