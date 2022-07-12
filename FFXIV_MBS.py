import requests
import json

f = open("market_items.json", "r")
market_items = json.load(f)

with open ('items.json') as file:
	items = json.load(file)

for x in range(1, len(market_items), 1):
	api_url = "https://universalis.app/api/v2/Ultros/" + str(market_items[x]) + "?listings=2"
	response = requests.get(api_url)
	price = response.json()
	if len(price['listings']) < 2:
		continue
	item_price1 = (price['listings'][0]['pricePerUnit'])
	item_price2 = (price['listings'][1]['pricePerUnit'])

	percentage = item_price1 - item_price2
	percentage = percentage / item_price2 * 100

	if abs(percentage) > 20:
		print(items[str(market_items[x])]["en"])
		print(item_price1)
		print(item_price2)
		print("%",abs(percentage))
		print(" ")

print("done!")