from to_db import *
from handle_sub import init_names_prices, get_price_item
from to_db import Prisjakt_DB


db = Prisjakt_DB

cursor = db.connect()


names, prices = init_names_prices(('RX', '6900', 'XT'))

vals = []
for i in range(len(names)):
    vals.append((names[i], prices[i]))

# keyword = "RX 6900 XT"
# category = 'Grafikkort'
# tup_names = []
# for i in range(len(names)):
#     tup_names.append((names[i], category, keyword))



# db.new_sub(tup_names, cursor, db)




