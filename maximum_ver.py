import requests
import operator
import copy
import json

with open ("market_items.json", encoding="utf8") as market_items: #open .json file with marketable item ID numbers
	market_items = json.load(market_items)

with open ('items.json', encoding="utf8") as all_items: #open .json file with all items names & ID numbers
	all_items = json.load(all_items)

#############
# variables #
#############
current_item_IDs = "2,"
# max_profit = 0

# dictionary = { #create temp dictionary
# 	"item_ID" : "1",
# 	"name" : "Gil",
# 	"u_price" : "0",
# 	"f_price" : "0",
# 	"exo_price" : "0",
# 	"b_price" : "0",
# 	"exc_price" : "0",
# 	"lam_price" : "0",
# 	"profit" : "0",
# 	"f_profit": "0",
# 	"b_profit": "0",
# 	"exo_profit": "0",
# 	"exc_profit": "0",
# 	"lam_profit": "0",
# 	"sv" : "0.0" 
# }

# max_profit_dictionary = { #create temp dictionary
# 	"item_ID" : "1",
# 	"name" : "Gil",
# 	"u_price" : "0",
# 	"f_price" : "0",
# 	"exo_price" : "0",
# 	"b_price" : "0",
# 	"exc_price" : "0",
# 	"lam_price" : "0",
# 	"profit" : "0",
# 	"f_profit": "0",
# 	"b_profit": "0",
# 	"exo_profit": "0",
# 	"exc_profit": "0",
# 	"lam_profit": "0",
# 	"sv" : "0.0" 
# }

for x in range(1, len(market_items)):
	current_item_IDs += str(market_items[x]) #add current item ID in market_items.json to long string of item IDs for mass API call
	current_item_IDs += "," #seperate each item ID by comma for API

	if x % 98 == 0: #API seems to only allow 99 request per call, so on 99th market_item.json ID added, make API call
		
		######API URLS FOR EACH WORD ON PRIMAL######
		api_url_ultros= "https://universalis.app/api/v2/Ultros/" + current_item_IDs + "?listings=2" #call api for current item(s)
		api_url_famfrit= "https://universalis.app/api/v2/Famfrit/" + current_item_IDs + "?listings=2"
		api_url_exodus= "https://universalis.app/api/v2/Exodus/" + current_item_IDs + "?listings=2"
		api_url_behemoth= "https://universalis.app/api/v2/Behemoth/" + current_item_IDs + "?listings=2"
		api_url_excalibur= "https://universalis.app/api/v2/Excalibur/" + current_item_IDs + "?listings=2"
		api_url_lamia= "https://universalis.app/api/v2/Lamia/" + current_item_IDs + "?listings=2"
		############################################
		world_prices_array = [9999999,9999999,9999999,9999999,9999999,9999999]
		profit_array = [0,0,0,0,0,0]
		world_quantities_array = [0,0,0,0,0,0]
		sale_velocity = 0.0

		######.JSON SETUPS FOR EACH WORD ON PRIMAL######
		ultros_response = requests.get(api_url_ultros) #set GET to response
		famfrit_response = requests.get(api_url_famfrit)
		exodus_response = requests.get(api_url_exodus)
		behemoth_response = requests.get(api_url_behemoth)
		excalibur_response = requests.get(api_url_excalibur)
		lamia_response = requests.get(api_url_lamia)
		ultros_prices = ultros_response.json() 
		famfrit_prices= famfrit_response.json()
		exodus_prices = exodus_response.json()
		behemoth_prices = behemoth_response.json()
		excalibur_prices = excalibur_response.json()
		lamia_prices = lamia_response.json()
		############################################

		current_item_IDs_list = current_item_IDs.split(",") #splitting up the long string of item IDs for easier data manipulation
		
		for z in range(0, len(current_item_IDs_list)-1):
			try:
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

				if len(behemoth_prices['items'][str(current_item_IDs_list[z])]['listings']) > 0:
					world_prices_array[3] = behemoth_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['pricePerUnit']
					world_quantities_array[3] = behemoth_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['quantity']

				if len(excalibur_prices['items'][str(current_item_IDs_list[z])]['listings']) > 0:
					world_prices_array[4] = excalibur_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['pricePerUnit']
					world_quantities_array[4] = excalibur_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['quantity']

				if len(lamia_prices['items'][str(current_item_IDs_list[z])]['listings']) > 0:
					world_prices_array[5] = lamia_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['pricePerUnit']
					world_quantities_array[5] = lamia_prices['items'][str(current_item_IDs_list[z])]['listings'][0]['quantity']

			except KeyError:
				continue

			if min(world_prices_array) < world_prices_array[0]: #if the minimum is less than ultros, continue
				percentage = world_prices_array[0] - min(world_prices_array)
				percentage = percentage / world_prices_array[0] * 100 #calculate percentage difference
				if abs(percentage) > 20 and float(sale_velocity) > 2: #if difference is greater than 20%, print out info to user
					
					# profit_array[0] = int((world_quantities_array[1] * world_prices_array[0])) - (world_prices_array[1] * world_quantities_array[1])
					# profit_array[1] = int((world_quantities_array[2] * world_prices_array[0])) - (world_prices_array[2] * world_quantities_array[2])
					# profit_array[2] = int((world_quantities_array[3] * world_prices_array[0])) - (world_prices_array[3] * world_quantities_array[3])
					# profit_array[3] = int((world_quantities_array[4] * world_prices_array[0])) - (world_prices_array[4] * world_quantities_array[4])
					# profit_array[4] = int((world_quantities_array[5] * world_prices_array[0])) - (world_prices_array[5] * world_quantities_array[5])

					# dictionary["item_ID"] = str(current_item_IDs_list[z])
					# dictionary["name"] = all_items[str(current_item_IDs_list[z])]["en"]
					# dictionary["u_price"] = world_prices_array[0]
					# dictionary["f_profit"] = profit_array[0]
					# dictionary["exo_profit"] = profit_array[1]
					# dictionary["b_profit"] = profit_array[2]
					# dictionary["exc_profit"] = profit_array[3]
					# dictionary["lam_profit"] = profit_array[4]
					# dictionary["f_price"] = world_prices_array[1]
					# dictionary["exo_price"] = world_prices_array[2]
					# dictionary["b_price"] = world_prices_array[3]
					# dictionary["exc_price"] = world_prices_array[4]
					# dictionary["lam_price"] = world_prices_array[5]
					# dictionary["sv"] = sale_velocity
					# dictionary["profit"] = max(profit_array)

					# if int(dictionary["profit"]) > max_profit:
					# 	max_profit_dictionary = copy.deepcopy(dictionary)
					# 	max_profit = int(dictionary["profit"])

					print(all_items[str(current_item_IDs_list[z])]["en"]) #name
					print("Ultros: ", world_prices_array[0], "Gil", "Quanitity:", world_quantities_array[0])
					print("Famfrit:", world_prices_array[1], "Gil", "Quanitity:", world_quantities_array[1], "Potential Profit:", "{:,}".format(int((world_quantities_array[1] * world_prices_array[0])) - (world_prices_array[1] * world_quantities_array[1])))
					print("Exodus: ", world_prices_array[2], "Gil", "Quanitity:", world_quantities_array[2], "Potential Profit:", "{:,}".format(int((world_quantities_array[2] * world_prices_array[0])) - (world_prices_array[2] * world_quantities_array[2])))
					print("Behemoth: ", world_prices_array[3], "Gil", "Quanitity:", world_quantities_array[3], "Potential Profit:", "{:,}".format(int((world_quantities_array[3] * world_prices_array[0])) - (world_prices_array[3] * world_quantities_array[3])))
					print("Excalibur: ", world_prices_array[4], "Gil", "Quanitity:", world_quantities_array[4], "Potential Profit:", "{:,}".format(int((world_quantities_array[4] * world_prices_array[0])) - (world_prices_array[4] * world_quantities_array[4])))
					print("Lamia: ", world_prices_array[5], "Gil", "Quanitity:", world_quantities_array[5], "Potential Profit:", "{:,}".format(int((world_quantities_array[5] * world_prices_array[0])) - (world_prices_array[5] * world_quantities_array[5])))
					print("Current Sale Velocity: ", sale_velocity)
					print("%",abs(percentage)," difference in price between minimum and Ultros")
					print(" ") #quantity * gil == net gain from purchase
		current_item_IDs = "" #empty ID string for next 99 entries

# print("___________________________________")
# print("Maximum Profit Item: ", max_profit_dictionary["name"])
# print("Maximum Possible Profit: ", max_profit_dictionary["profit"])
# print("Ultros: ", max_profit_dictionary["u_price"])
# print("Famfrit: ", max_profit_dictionary["f_price"], "Profit: ", max_profit_dictionary["f_profit"])
# print("Behemoth: ", max_profit_dictionary["b_price"], "Profit: ", max_profit_dictionary["b_profit"])
# print("Exodus: ", max_profit_dictionary["exo_price"], "Profit: ", max_profit_dictionary["exo_profit"])
# print("Lamia: ", max_profit_dictionary["lam_price"], "Profit: ", max_profit_dictionary["lam_profit"])
# print("Excalibur: ", max_profit_dictionary["exc_price"], "Profit: ", max_profit_dictionary["exc_profit"])
# print("Sale Velocity: ", max_profit_dictionary["sv"])
# print("___________________________________")

print("FINISHED!")
