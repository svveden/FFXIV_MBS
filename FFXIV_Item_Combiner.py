#This program is for taking the .json dump of ALL in-game items,
#and combining it with the Universalis API marketable items (which is just their item IDs)
#This outputs a file, "new_items.json", which is a json file with marketable
#item's IDs and names for easier future changes.
import json

with open ("market_items.json") as f1: #open file containing marketable items
	market_items = json.load(f1)

with open ("items.json") as f2: #open file containing ALL items
	items = json.load(f2)

dictionary = { #create temp dictionary
	"item_ID" : "1",
	"name" : "Gil" 
}

f3 = open ("new_items.json", "a") #create new file
item_keys = items.keys()

for x in range(0, len(market_items)): #for all numbers in marketable items
	dictionary["item_ID"] = str(market_items[x]) #set dict to ID, and name from items.json
	dictionary["name"] = items[str(market_items[x])]["en"]
	json_object = json.dumps(dictionary) #dump to a dictionary json object
	f3.write(json_object) #output to file

f1.close() #close for safety
f2.close()
f3.close()