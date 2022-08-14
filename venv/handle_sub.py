import bs4, requests, re


def init_names_prices(*args):
    # creates the tail for the url from keywords
    space = '%20'
    phrase = str(args[0])
    for word in range(1, len(args)):
        phrase = phrase + space
        phrase = phrase + str(args[word])
    
    # creats doc object from searching prisjakt with keywords
    link = f"https://www.prisjakt.nu/search?search={phrase}"
    res = requests.get(link)

    # uses html to get the top 10 result name, sorted by best hits
    pj_search_res = bs4.BeautifulSoup(res.text, 'html.parser')
    pj_item_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .kBBoFI')
    item_name_list = [x.getText() for x in pj_item_list]
    item_name_list = item_name_list[:10]

    # uses html to get the top 10 result prices, sorted by best hits and converted to int
    pj_price_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .PriceContainer-sc-rdha17-0 .duGKvV')
    item_price_list = [x.getText() for x in pj_price_list]
    item_price_list = item_price_list[:10]
    item_price_list = [int(''.join(re.findall(r'\d+', x))) for x in item_price_list]
    
    return item_name_list, item_price_list


def get_price_item(item_name):
    # gets item from DB and returns top three results along with names
    space = '%20'
    split_name = item_name.split(' ')
    phrase = space.join(split_name)
    name_list = []

    # creates link and documnet
    link = f"https://www.prisjakt.nu/search?search={phrase}"
    res = requests.get(link)
    pj_search_res = bs4.BeautifulSoup(res.text, 'html.parser')
    pj_item_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .kBBoFI')
    
    # gets text and top three results
    item_name_list = [x.getText() for x in pj_item_list]
    item_name_list = item_name_list[:3]

    # loops through the three results to se if they match more than 80% of the loaded name
    for i in item_name_list:
        hit_count = 0
        for j in split_name:
            if j in i:
                hit_count += 1
        if hit_count / len(split_name) > 0.8:
            name_list.append(i)

    pj_price_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .PriceContainer-sc-rdha17-0 .duGKvV')
    price_list = [x.getText() for x in pj_price_list]
    price_list = price_list[:len(name_list)]
    price_list = [int(''.join(re.findall(r'\d+', x))) for x in price_list]

    return name_list, price_list



class subscribe_prisjakt:
    # creats object using above functions to feed into DB and feed from DB to subscribe prices

    def __init__(self, *args) -> None:
        # initial search keywords
        self.item_name, self.item_prices = init_names_prices(args)


x = 'Asus Radeon RX 6900 XT ROG Strix Gaming LC Topf HDMI 2xDP 16GB'
y_list = ['Asus Radeon RX 6900 XT ROG Strix Gaming LC Top HDMI 2xDP 16GB', 
'Asus Radeon RX 6900 XT ROG Strix Gaming LC OC HDMI 2xDP 16GB', 
'Tomtefar Radeon RX 6700 XT Gaming HDMI 2xDP 12GB']

