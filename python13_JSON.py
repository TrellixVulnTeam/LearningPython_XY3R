# Example file for parsing and processing JSON

import urllib.request
import json

# def printResults(data):
    # Use the json module to load the string data into a dictionary
    # theJSON = json.loads(data)
    # Now we can access the contents of the JSON like any other Python objects
    # if "title" in theJSON["metadata"]:
    #     print(theJSON["metadata"]["title"])

    # Output the number of events, plus the magnitutde and eah event name
    # count = theJSON["metadata"]["count"]
    # print (str(count) + " events recorded")
    # For each events, print the place where it occurred
    # for i in theJSON["features"]:
    #     print(i["properties"]["place"])
    # print("-----------------------\n")
    # Print the events that only have a magntutde greater than 4
    # for i in theJSON["features"]:
    #     if i["properties"]["mag"]  >= 4.0:
    #         print(i["properties"]["mag"], i["properties"]["place"]) 
    # print("-----------------------\n")
    
def main():
    # Defie a varable to hold the soruce URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than mag 2.5
    urlData = "https://api.worldoftanks.eu/wot/account/list/?language=en&application_id=demo&search=Donadelo"

    webUrl = urllib.request.urlopen(urlData)

    if (webUrl.getcode() == 200):
        data = webUrl.read()
        # printResults(data)
        print(data)
        print("Status OK ^_^ \n")
    else: 
        print("Recieved error, can not parse results")
main()