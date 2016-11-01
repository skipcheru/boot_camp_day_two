
import urllib.request
import json

""" Consume public api data here"""

def consume_maps():

    county = input("Hi enter the town you want to search in Kenya: ")

    api_key = 'AIzaSyBQC8Pxyu_dyOnDvs5lhGnBSUjCFRp8jpc' #google api key

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + county + '+county+kenya&key=' + api_key

    response = urllib.request.urlopen(url)

    contents = response.read()

    res_text = contents.decode('UTF-8')  #get the correct mime type

    data = json.loads(res_text)

    # print(data) debug json output

    """If google finds the county print few county info, else regret"""
    if data["status"] == "OK":
        for town in data['results']:
            # print(town['place_id'])
            print("Yes your county is in ",
                  town['address_components'][1]['long_name'])
            print("Your county details")
            print("Name : ",
                  town['address_components'][0]['short_name'])
            print("Coordinates :",
                  town['geometry']['location']['lng'],
                  " East",
                  town['geometry']['location']['lat'], "South", )

            print("County places id ",
                  town['place_id'])

            print("Bye for Now!")

    else:
        print("Sorry I didn't find your town")

consume_maps()
