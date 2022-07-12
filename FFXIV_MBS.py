import requests
import json


with open ("market_items.json", "r") as market_items: #open .json file with marketable item ID numbers
	market_items = json.load(market_items)

with open ('items.json') as all_items: #open .json file with all items names & ID numbers
	all_items = json.load(all_items)

for x in range(1, len(market_items), 1): #for all items in market_items.json
	api_url = "https://universalis.app/api/v2/Ultros/" + str(market_items[x]) + "?listings=2" #call api for current item
	
	response = requests.get(api_url) #set GET to response
	
	price = response.json()
	
	if len(price['listings']) < 2: #if there are less than 2 listings for this item, skip
		continue
	
	item_price1 = (price['listings'][0]['pricePerUnit'])
	item_price2 = (price['listings'][1]['pricePerUnit'])

	percentage = item_price1 - item_price2 
	percentage = percentage / item_price2 * 100 #calculate percentage difference

	if abs(percentage) > 20: #if difference is greater than 20%, print out info to user		 
		print(all_items[str(market_items[x])]["en"]) #name
		print(item_price1)
		print(item_price2)
		print("%",abs(percentage))
		print(" ")

print("done!")
