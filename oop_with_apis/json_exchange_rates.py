# import json
# create a class Exchange_rates
# with required attributes
# fetch the data from exchange_rates.json
# display the data
# display the type of the data
# method to return the exchange rates
# display the exchange rates with specific currencies

import json

class Exchange_Rates:
    def __init__(self):
        # opens the associated "exchange_rates.json" that was made previously
        with open("exchange_rates.json", "r") as exchange_files:
            # variable created from saved file exchange_rates.json
            data = json.load(exchange_files)
            for a in data:
                if a == "base":
                    print(data)
            currency = input(
                "What currency would you like the exchange rate of, please see list.\n")
            # /n is for next line to add input

            # display exchange rates with specific currencies
            print("The exchange rate", currency, "is", data["rates"][currency])


            # print(data)
a = Exchange_Rates
a.__init__(Exchange_Rates)
