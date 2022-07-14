import requests
import json

with open ("market_items.json", encoding="utf8") as market_items: #open .json file with marketable item ID numbers
	market_items = json.load(market_items)

with open ('items.json', encoding="utf8") as all_items: #open .json file with all items names & ID numbers
	all_items = json.load(all_items)

#############
# variables #
#############
current_item_IDs = "2,"

current_greatest = 0
current_greatest_percentage = ""
second_greatest = 0
second_greatest_percentage = ""

for x in range(1, len(market_items)):
	current_item_IDs += str(market_items[x]) #add current item ID in market_items.json to long string of item IDs for mass API call
	current_item_IDs += "," #seperate each item ID by comma for API

	if x % 98 == 0: #API seems to only allow 99 request per call, so on 99th market_item.json ID added, make API call
		
		######API URLS FOR EACH WORD ON PRIMAL######
		api_url_ultros= "https://universalis.app/api/v2/Ultros/" + current_item_IDs + "?listings=2" #call api for current item(s)
		api_url_famfrit= "https://universalis.app/api/v2/Famfrit/" + current_item_IDs + "?listings=2"
		api_url_exodus= "https://universalis.app/api/v2/Exodus/" + current_item_IDs + "?listings=2"
		############################################
		world_prices_array = [9999999,9999999,9999999]
		world_quantities_array = [0,0,0]
		sale_velocity = 0.0

		######.JSON SETUPS FOR EACH WORD ON PRIMAL######
		ultros_response = requests.get(api_url_ultros) #set GET to response
		famfrit_response = requests.get(api_url_famfrit)
		exodus_response = requests.get(api_url_exodus)
		ultros_prices = ultros_response.json() 
		famfrit_prices= famfrit_response.json()
		exodus_prices = exodus_response.json()
		############################################

		current_item_IDs_list = current_item_IDs.split(",") #splitting up the long string of item IDs for easier data manipulation
		
		for z in range(0, len(current_item_IDs_list)-1):
			if len(ultros_prices['items'][str(current_item_IDs_list[z])]['listings']) > 0: #if there are less than 1 listings for this item, skip
				world_prices_array[0] = ultros_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['pricePerUnit']
				world_quantities_array[0] = ultros_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['quantity']
				sale_velocity = ultros_prices['items'][str(current_item_IDs_list[z])]['regularSaleVelocity']
			if len(famfrit_prices['items'][str(current_item_IDs_list[z])]['listings']) > 0:
				world_prices_array[1] = famfrit_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['pricePerUnit']
				world_quantities_array[1] = famfrit_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['quantity']
			if len(exodus_prices['items'][str(current_item_IDs_list[z])]['listings']) > 0:
				world_prices_array[2] = exodus_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['pricePerUnit']
				world_quantities_array[2] = exodus_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['quantity']

			if min(world_prices_array) < world_prices_array[0]: #if the minimum is less than ultros, continue
				percentage = world_prices_array[0] - min(world_prices_array)
				percentage = percentage / world_prices_array[0] * 100 #calculate percentage difference
				#print(percentage)
				if abs(percentage) > 20 and float(sale_velocity) > 2: #if difference is greater than 20%, print out info to user
					print(all_items[str(current_item_IDs_list[z])]["en"]) #name
					print("Ultros: ", world_prices_array[0], "Gil", "Quanitity:", world_quantities_array[0])
					print("Famfrit:", world_prices_array[1], "Gil", "Quanitity:", world_quantities_array[1], "Potential Profit:", "{:,}".format(int((world_quantities_array[1] * world_prices_array[0])) - (world_prices_array[1] * world_quantities_array[1])))
					print("Exodus: ", world_prices_array[2], "Gil", "Quanitity:", world_quantities_array[2], "Potential Profit:", "{:,}".format(int((world_quantities_array[2] * world_prices_array[0])) - (world_prices_array[2] * world_quantities_array[2])))
					print("Current Sale Velocity: ", sale_velocity)
					print("%",abs(percentage)," difference in price between minimum and Ultros")
					print(" ") #quantity * gil == net gain from purchase
		current_item_IDs = "" #empty ID string for next 99 entries

print(largest_profit)
print("FINISHED!")
