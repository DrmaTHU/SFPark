import json
import time
import requests

'''
This is the web_crawler for SF park.
The location is San Francisco Downtown Area

@params1 is set to crawl general traffic congestion information

'''

param1 = {'lat': '37.788421', 
          'long' : '-122.387831', 
          'radius' : '1.5', 
          'uom' : 'mile',
          'response' : 'json',
          'pricing' : 'no'  }


requests.adapters.DEFAULT_RETRIES = 10

#the url string for SF park
url = "http://api.sfpark.org/sfpark/rest/availabilityservice"

#counter of request numbers
i = 1

#the seat availability file

while True:
    strdate = time.strftime("%m%d%Y")
    filename_park = 'SF_'+strdate + '_parkEZ_noRate.txt'
    avalfile = open(filename_park,"a")

    seatavail = requests.get(url, params = param1)
    try:
           javal = json.loads(seatavail.text)
    except ValueError:
            continue
    else:
         if javal['STATUS'] == 'SUCCESS':
             for avl in javal['AVL']:
                 try:
                     park_type = avl['TYPE']
                 except KeyError:
                     continue
                 else:
                     if park_type == 'OFF':
                         try:
                             templength = len(avl['OSPID'])
                             templength = len(avl['OPER'])
                             templength = len(avl['OCC'])
                             templength = len(avl['LOC'])
                         except KeyError:
                             continue
                         else:
							 avalfile.write(javal['AVAILABILITY_UPDATED_TIMESTAMP'] + ', ')
							 avalfile.write(avl['OSPID'] + ', ')
							 avalfile.write(avl['OPER'] + ', ')
							 avalfile.write(avl['OCC'] + ', ')
							 avalfile.write(avl['TYPE']+ ', ')
							 avalfile.write(avl['NAME']+ ', ')
							 avalfile.write(avl['TEL']+ ', ')
							 avalfile.write(avl['INTER']+ ', ')
							 avalfile.write(avl['DESC']+ ', ')
							 avalfile.write(avl['PTS']+ ', ')
							 avalfile.write(avl['LOC']+ ', ')
							 avalfile.write('\n')
                     if park_type == 'ON':
                         try:
                             templength = len(avl['BFID'])
                             templength = len(avl['OPER'])
                             templength = len(avl['OCC'])
                             templength = len(avl['LOC'])
                         except KeyError:
                             continue
                         else:
                             if avl['OPER'] != "0":
                                #avalfile.write('{"TIME": "')
                                avalfile.write(javal['AVAILABILITY_UPDATED_TIMESTAMP'] + ', ')
                                #avalfile.write('"BFID": "')
                                avalfile.write(avl['BFID'] + ', ')
                                #avalfile.write('"OPER": "')
                                #avalfile.write(avl['OPER'] + ', ')
                                #avalfile.write('"OCC": "')
                                #avalfile.write(avl['OCC'] + '", ')
                                #avalfile.write('"TYPE": "')
                                avalfile.write(avl['TYPE']+ ', ')
                                #avalfile.write('"LOC": "')
                                avalfile.write(avl['LOC']+ ',')
                                avalfile.write('\n')
             #avalfile.write(json.dumps(avl) + '\n')
    time.sleep(60*5)
    i = i + 1
    #if i > 600:
        #break
